# Generated by Django 5.1.3 on 2024-11-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0025_profile_organization_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
    ]