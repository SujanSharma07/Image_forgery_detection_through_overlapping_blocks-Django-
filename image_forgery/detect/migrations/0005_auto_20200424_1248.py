# Generated by Django 3.0.5 on 2020-04-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detect', '0004_auto_20200424_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectedimages',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
