# Generated by Django 3.1.13 on 2021-12-12 20:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20211201_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Минимальное количество ингредиента - 0')], verbose_name='Количество игредиента'),
        ),
    ]