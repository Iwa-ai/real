# Generated by Django 3.0.3 on 2020-06-04 15:11

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_remove_post_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=stdimage.models.StdImageField(blank=True, default='japan', upload_to='img/'),
            preserve_default=False,
        ),
    ]
