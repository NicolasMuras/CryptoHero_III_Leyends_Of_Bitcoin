# Generated by Django 3.1.6 on 2021-02-14 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20210213_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='songs.artist', verbose_name='Autor'),
            preserve_default=False,
        ),
    ]