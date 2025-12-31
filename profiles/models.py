from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.files.base import ContentFile
import uuid
import os
from io import BytesIO
from PIL import Image
# unique path for profile pictures


def profile_pic_path(instance, filename):
    return os.path.join('profile_pics', filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=profile_pic_path,
        default='profile_pics/default.jpg',
        blank=True,
        null=True,
        max_length=255
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        
        # Check if the image is new (unsaved file)
        if self.pk and hasattr(self.image, "file") and not getattr(self.image.file, "temporary_file_path", None):
            # Image already exists on model → do NOT compress again
            return super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            img.thumbnail((800, 800))

            img_io = BytesIO()
            img.save(img_io, format="JPEG", quality=70, optimize=True)

            # Generate unique name
            filename = f"{uuid.uuid4()}.jpg"

            # Replace original upload BEFORE Django saves it
            self.image = ContentFile(img_io.getvalue(), name=filename)

        super().save(*args, **kwargs)


# Create profile automatically when a new user is created


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Create a profile for new users
        Profile.objects.create(user=instance)
