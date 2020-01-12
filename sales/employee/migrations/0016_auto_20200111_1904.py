# Generated by Django 3.0.1 on 2020-01-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_auto_20200111_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callallocation',
            name='status',
            field=models.CharField(blank=True, choices=[('not_yet', 'Not Yet'), ('in_progress', 'In Progress'), ('on_hold', 'On hold'), ('completed', 'Completed')], max_length=15),
        ),
    ]
