# Generated by Django 5.1.3 on 2024-11-26 04:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0023_alter_profile_profile_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="address",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="birthday",
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
            name="organization_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="phone_number",
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="static/images/profile_pics/"
            ),
        ),
    ]