# Generated by Django 4.1 on 2023-11-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddff', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
