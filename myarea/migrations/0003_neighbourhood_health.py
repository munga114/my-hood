# Generated by Django 4.0.5 on 2022-06-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myarea', '0002_remove_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='health',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
