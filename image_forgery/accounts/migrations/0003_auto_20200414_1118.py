# Generated by Django 3.0.5 on 2020-04-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200412_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_form',
            name='signup_date',
        ),
        migrations.AlterField(
            model_name='user_form',
            name='image',
            field=models.ImageField(default='', upload_to='home/sujan/PycharmProjects/learndjango/image_forgery/accounts/media'),
        ),
    ]
