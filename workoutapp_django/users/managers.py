from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, email, **extra_fields):
        user = self.model(username, password, email)
        user.password
        user.save()
        return user

    def create_superuser(self, username, password, email, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, password, email, **extra_fields)