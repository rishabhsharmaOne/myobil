from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, mobile_no, password=None, **extra_fields):
        """
        Creates and saves a new user with the provided email and password.

        :param email: The email address of the user.
        :param mobile_no: The mobile number of the user.
        :param password: The password for the user. If not provided, a random password is generated.
        :param extra_fields: Additional fields to be included in the user model.
        :raises ValueError: If the email or mobile_no field is not provided.
        :return: The newly created user.
        """
        if not email:
            raise ValueError("Email field must be set")
        if not mobile_no:
            raise ValueError("Mobile number field must be set")

        email = self.normalize_email(email)
        
        user = self.model(email=email, mobile_no=mobile_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email,mobile_no, password=None, **extra_fields):
        """
        Creates and saves a new superuser with the provided email and password.

        :param email: The email address of the superuser.
        :param password: The password for the superuser. If not provided, a random password is generated.
        :param extra_fields: Additional fields to be included in the superuser model.
        :raises ValueError: If is_staff or is_superuser is not explicitly set to True.
        :return: The newly created superuser.
        """

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, mobile_no, password, **extra_fields)
