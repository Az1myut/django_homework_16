# Generated by Django 4.1.5 on 2023-01-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_alter_classbyday_options_remove_classbyday_name_and_more'),
        ('students', '0003_student_on_class_alter_student_groupe'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_day',
            field=models.ManyToManyField(related_name='class_day', to='classes.classbyday', verbose_name='День недели'),
        ),
    ]