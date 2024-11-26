# Generated by Django 5.1.3 on 2024-11-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_alter_customer_options_alter_shippingaddress_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="birthdate",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="profile_image",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="store_name",
        ),
        migrations.AddField(
            model_name="profile",
            name="photo",
            field=models.ImageField(default="default.jpg", upload_to="profile_pics/"),
        ),
    ]
