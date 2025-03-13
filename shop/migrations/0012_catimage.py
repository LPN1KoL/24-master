# Generated by Django 4.2.17 on 2024-12-21 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_customuser_email_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cat_images', verbose_name='Картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
        ),
    ]
