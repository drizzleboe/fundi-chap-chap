# Generated by Django 4.0.1 on 2022-02-06 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_users_prfssn'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=20)),
                ('user_name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('passwd', models.CharField(max_length=50, null='False')),
                ('age', models.CharField(max_length=4)),
                ('slug', models.CharField(max_length=30, unique=True)),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.region')),
                ('prfssn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.profession')),
            ],
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
