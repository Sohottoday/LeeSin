# Generated by Django 2.1.15 on 2020-06-30 10:24

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillstack',
            name='img',
            field=imagekit.models.fields.ProcessedImageField(default='icon/dummy.png', upload_to='icon'),
        ),
    ]
