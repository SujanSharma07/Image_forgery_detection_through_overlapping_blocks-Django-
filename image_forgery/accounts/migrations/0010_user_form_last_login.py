# Generated by Django 3.0.5 on 2020-04-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_user_form_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_form',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
