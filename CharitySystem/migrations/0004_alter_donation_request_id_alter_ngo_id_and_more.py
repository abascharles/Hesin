# Generated by Django 5.0 on 2023-12-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharitySystem', '0003_donation_request_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation_request',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='verification_status',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
