# Generated by Django 3.2.25 on 2024-05-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPV_app', '0003_auto_20240509_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_requisition',
            name='Which',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]