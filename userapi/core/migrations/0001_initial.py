# Generated by Django 3.2.6 on 2021-08-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(auto_now=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('height', models.CharField(blank=True, max_length=50, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=50, null=True)),
                ('alcohol', models.BooleanField(default=False)),
                ('smoke', models.BooleanField(default=False)),
                ('relationship', models.CharField(blank=True, max_length=50, null=True)),
                ('languages', models.CharField(blank=True, max_length=50, null=True)),
                ('update_date', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]
