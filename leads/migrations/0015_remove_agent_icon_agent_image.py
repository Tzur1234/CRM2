# Generated by Django 4.1.7 on 2023-03-13 11:46

from django.db import migrations, models
import leads.models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0014_alter_areacode_country_followup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='icon',
        ),
        migrations.AddField(
            model_name='agent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=leads.models.agent_folder_path),
        ),
    ]
