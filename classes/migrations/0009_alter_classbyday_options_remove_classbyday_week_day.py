# Generated by Django 4.1.5 on 2023-01-26 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_alter_classbyday_options_remove_classbyday_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classbyday',
            options={'verbose_name': 'Дни недели', 'verbose_name_plural': 'Дни недели'},
        ),
        migrations.RemoveField(
            model_name='classbyday',
            name='week_day',
        ),
    ]
