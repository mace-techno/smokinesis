# Generated by Django 4.1.2 on 2022-10-28 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_useraccount_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='tranxid',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
