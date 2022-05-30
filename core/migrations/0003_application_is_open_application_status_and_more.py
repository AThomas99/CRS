# Generated by Django 4.0.4 on 2022-05-29 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='interest',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=70)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.course')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='student_rating', to='core.student')),
            ],
        ),
    ]
