# Generated by Django 3.2.25 on 2024-05-15 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SPV_app', '0006_alter_conditions_of_employment_duration_of_engagement'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Human_Resources',
            new_name='Data_of_selected_personnel',
        ),
    ]