# Generated by Django 5.0.4 on 2024-08-10 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floriCultura', '0021_remove_address_state_city_state_state_uf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='state',
            name='updated_at',
        ),
    ]
