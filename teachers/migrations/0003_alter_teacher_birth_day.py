# Generated by Django 4.1.5 on 2023-01-11 17:53

from django.db import migrations, models
import teachers.validators.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teacher_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth_day',
            field=models.DateField(auto_now_add=True, validators=[teachers.validators.validators.validate_age], verbose_name='Дата рождения'),
        ),
    ]
