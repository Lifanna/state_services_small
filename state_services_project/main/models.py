from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number or password is None:
            raise ValueError('Phone number is required field.')

        # phone_number = self.normalize_email(phone_number)
        user = self.model(phone_number=phone_number, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        if not phone_number or password is None:
            raise ValueError('Required.')

        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True

        # phone_number = self.normalize_email(phone_number)
        user = self.model(phone_number=phone_number, **extra_fields)

        user.set_password(password)
        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=50, unique=True)

    first_name = models.CharField(max_length=12, verbose_name='Имя', null=True)
    
    last_name = models.CharField(max_length=12, verbose_name='Фамилия', null=True)
    
    is_active = models.BooleanField(default=True, verbose_name='Прошел активацию')
    
    is_staff = models.BooleanField(default=False, verbose_name='Служебный аккаунт')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_perm(*args, **kwargs):
        return True

    def has_module_perms(*args, **kwargs):
        return True

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Letter(models.Model):
    LETTER_CHOICES = (
        ('Госпочта', 'Госпочта'),
        ('Платеж', 'Платеж'),
    )

    letter_type = models.CharField("Направление", max_length=20, choices=LETTER_CHOICES)

    topic = models.CharField("Тема", max_length=255)

    created_at = models.DateTimeField(verbose_name='Дата создания')
    
    obtained_at = models.DateTimeField(verbose_name="Дата вручения", null=True)

    updated_at = models.DateTimeField(auto_now=True)

    text = models.TextField("Текст")

    footer_text = models.TextField("Текст подвала")

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"

class Debt(models.Model):
    text = models.TextField("Задолженность")

    debt_sum = models.FloatField("Сумма задолженности", default=0)

    class Meta:
        verbose_name = "Задолженность"
        verbose_name_plural = "Задолженность"
