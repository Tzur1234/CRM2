# Generated by Django 4.1.7 on 2023-03-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
