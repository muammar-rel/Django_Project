# Generated by Django 5.1.3 on 2024-11-25 22:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0016_alter_profile_email_address_alter_profile_first_name_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="email_address",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="location",
        ),
        migrations.AddField(
            model_name="profile",
            name="address",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="profile",
            name="organization_name",
            field=models.CharField(blank=True, default="Unknown", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(blank=True, default="Unknown", max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pictures/"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
