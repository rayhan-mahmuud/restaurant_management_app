from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

ROLES = (
    ('manager', 'Manager'),
    ('cashier', 'Cashier'),
    ('chef', 'Chef'),
    ('waiter', 'Waiter'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile-pic.jpg', upload_to='profile_pictures/')
    gender = models.CharField(max_length=100, choices=GENDER)
    role = models.CharField(max_length=150, choices=ROLES)
    location = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user.username}'s profile"

