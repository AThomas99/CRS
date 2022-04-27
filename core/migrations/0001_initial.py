# Generated by Django 4.0.4 on 2022-04-26 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NectaBasicInfoAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('CSEE', models.CharField(max_length=200)),
                ('ASCEE', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NectaCSEEReusltsAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physics', models.CharField(max_length=10)),
                ('chemisty', models.CharField(max_length=10)),
                ('biology', models.CharField(max_length=10)),
                ('maths', models.CharField(max_length=10)),
                ('english', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('CSEE', models.CharField(max_length=200)),
                ('ASCEE', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('profile_pic', models.ImageField(blank=True, default='user-1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]