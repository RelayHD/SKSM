# Generated by Django 4.0 on 2021-12-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textrow',
            name='row_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
