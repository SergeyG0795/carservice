# Generated by Django 5.0.4 on 2024-05-22 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_category_service_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
    ]