# Generated by Django 4.1.7 on 2023-03-06 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='oraganization',
            new_name='organization',
        ),
    ]