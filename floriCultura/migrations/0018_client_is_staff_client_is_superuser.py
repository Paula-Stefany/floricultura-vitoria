# Generated by Django 5.0.4 on 2024-08-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floriCultura', '0017_client_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]