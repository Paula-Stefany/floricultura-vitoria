# Generated by Django 5.0.4 on 2024-05-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floriCultura', '0012_neighborhood_alter_address_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]