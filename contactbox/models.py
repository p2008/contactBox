from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    description = models.TextField(null=True)
    address = models.ManyToManyField('Address', related_name='user')
    group = models.ManyToManyField('Group', related_name='users')


class Address(models.Model):
    city = models.CharField(max_length=128, null=False)
    street = models.CharField(max_length=128, null=False)
    house_number = models.CharField(max_length=16, null=False)
    flat_number = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, message='Minimal value must be 1')
        ],
        null=True
    )


class Phone(models.Model):
    phone_number = PhoneNumberField(unique=True, null=False)
    phone_type = models.CharField(max_length=32, null=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE,
                             related_name='phones', null=False)


class Email(models.Model):
    email = models.EmailField(unique=True, null=False)
    email_type = models.CharField(max_length=32, null=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE,
                             related_name='emails', null=False)


class Group(models.Model):
    group_name = models.CharField(max_length=32, null=False)



    # CHOICES = [
    #     'home',
    #     'work',
    #     'mobile',
    #     'home fax',
    #     'work fax',
    #     'pager',
    #     'other',
    #     'own',
    # ]
