# Generated by Django 3.0.5 on 2020-04-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_form_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_form',
            name='signup_date',
        ),
    ]
