# Generated by Django 5.1.2 on 2024-10-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gimg', models.ImageField(upload_to='gpics')),
                ('gname', models.CharField(max_length=250)),
                ('gdesign', models.CharField(max_length=250)),
            ],
        ),
    ]