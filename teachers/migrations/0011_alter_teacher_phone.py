# Generated by Django 4.1.5 on 2023-01-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_remove_teacher_to_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=14, verbose_name='Телефон'),
        ),
    ]
