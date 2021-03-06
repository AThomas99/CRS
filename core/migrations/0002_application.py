# Generated by Django 4.0.4 on 2022-05-26 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_choice1', to='core.course')),
                ('choice2', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_choice2', to='core.course')),
                ('choice3', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_choice3', to='core.course')),
                ('choice4', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_choice4', to='core.course')),
                ('choice5', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_choice5', to='core.course')),
                ('choice6', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_choice6', to='core.course')),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_course', to='core.student')),
            ],
        ),
    ]
