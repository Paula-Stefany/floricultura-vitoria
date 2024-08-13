# Generated by Django 5.0.4 on 2024-08-10 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floriCultura', '0020_remove_client_email_remove_client_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities', to='floriCultura.state'),
        ),
        migrations.AddField(
            model_name='state',
            name='uf',
            field=models.CharField(max_length=5, null=True, unique=True),
        ),
    ]