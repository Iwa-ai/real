# Generated by Django 3.0.3 on 2020-06-04 15:29

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_auto_20200605_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=stdimage.models.StdImageField(blank=True, upload_to='path/to/img'),
        ),
    ]