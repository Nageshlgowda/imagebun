# Generated by Django 4.1.4 on 2022-12-30 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgbun', '0002_alter_imgdb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgdb',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]