# Generated by Django 5.1.3 on 2024-11-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0013_rename_userprofile_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_picture",
            field=models.ImageField(default="default.png", upload_to="profile_pics/"),
        ),
    ]