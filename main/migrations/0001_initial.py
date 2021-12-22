# Generated by Django 4.0 on 2021-12-21 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField()),
                ('first_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Textrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_number', models.IntegerField()),
                ('paragraph_1', models.TextField(blank=True, null=True)),
                ('paragraph_2', models.TextField(blank=True, null=True)),
                ('paragraph_3', models.TextField(blank=True, null=True)),
                ('paragraph_4', models.TextField(blank=True, null=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textrow', to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main/images/%Y/%m/%d/')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.textrow')),
            ],
        ),
    ]