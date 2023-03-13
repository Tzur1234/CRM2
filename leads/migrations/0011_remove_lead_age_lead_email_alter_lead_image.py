# Generated by Django 4.1.7 on 2023-03-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='age',
        ),
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='image',
            field=models.ImageField(upload_to='profile_picture'),
        ),
    ]
