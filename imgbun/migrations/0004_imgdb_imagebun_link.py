# Generated by Django 4.1.4 on 2022-12-30 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgbun', '0003_imgdb_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgdb',
            name='imagebun_link',
            field=models.URLField(default='http://127.0.0.1:8000/'),
        ),
    ]
