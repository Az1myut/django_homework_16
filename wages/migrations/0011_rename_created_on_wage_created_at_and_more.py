# Generated by Django 4.1.5 on 2023-01-24 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wages', '0010_remove_wage_date_wage_created_on_wage_edited_on_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wage',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='wage',
            old_name='edited_on',
            new_name='updated_at',
        ),
    ]
