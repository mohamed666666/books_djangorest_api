# Generated by Django 4.2.2 on 2023-07-02 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0002_appuser_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='user_id',
            new_name='id',
        ),
    ]