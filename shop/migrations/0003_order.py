# Generated by Django 5.1.1 on 2024-09-12 14:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_product_tag_alter_role_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacts', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Контакты заказчика')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Оформлен')),
                ('status', models.CharField(choices=[('Подан', '1'), ('На рассмотрении', '2'), ('Принят', '3'), ('Выполняется', '4'), ('Готов', '5')], max_length=100, verbose_name='Статус заказа')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]