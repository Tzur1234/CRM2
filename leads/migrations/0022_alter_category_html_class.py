# Generated by Django 4.1.7 on 2023-03-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0021_lead_converted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='html_class',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
