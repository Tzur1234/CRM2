# Generated by Django 4.1.7 on 2023-03-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0015_remove_agent_icon_agent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='html_class',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]