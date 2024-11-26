# Generated by Django 5.1.3 on 2024-11-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_remove_customer_email_remove_customer_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="address",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="phone_number",
        ),
        migrations.AddField(
            model_name="customer",
            name="email",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]