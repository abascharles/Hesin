# Generated by Django 5.0 on 2023-12-10 14:57

import django_currentuser.middleware
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharitySystem', '0004_alter_donation_request_id_alter_ngo_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(blank=True, max_length=30)),
                ('domain', models.CharField(blank=True, max_length=20)),
                ('head_of_club', models.CharField(blank=True, max_length=30)),
                ('contactNo', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('registration_cerificate_Trust_Society', models.FileField(blank=True, upload_to='verification')),
                ('certificate_12A', models.FileField(blank=True, upload_to='verification')),
                ('beneficiary_profiles', models.FileField(blank=True, upload_to='verification')),
                ('verification_status', models.BooleanField(blank=True, default=None, null=True)),
                ('ngo_current_user', models.CharField(blank=True, default=django_currentuser.middleware.get_current_authenticated_user, max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='NGO',
        ),
    ]
