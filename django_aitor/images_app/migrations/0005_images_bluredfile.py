# Generated by Django 4.1.5 on 2023-02-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_app', '0004_alter_images_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='bluredfile',
            field=models.ImageField(default='', upload_to='pics'),
            preserve_default=False,
        ),
    ]