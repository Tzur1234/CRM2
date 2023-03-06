# Generated by Django 4.1.7 on 2023-03-06 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_user_is_agent_alter_user_is_organizor'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent'),
        ),
    ]