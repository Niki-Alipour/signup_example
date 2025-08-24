from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'customer'),
        (2, 'service_provider'),
        (3, 'manager'),
    )
    ROLE_CHOICES = (
        ('service_provider','service_provider'),
        ('customer', 'customer'),
        ('seller', 'seller'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    phone = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.username


    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    is_premium = models.BooleanField(default=False)
    premium_expiry = models.DateField(null=True, blank=True)
    
    def can_access_chat(self):
        return self.is_premium and (self.premium_expiry is None or self.premium_expiry > timezone.now().date())