# Generated by Django 3.2.9 on 2021-11-17 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211117_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.post'),
        ),
    ]
