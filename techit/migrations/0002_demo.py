# Generated by Django 3.2.9 on 2021-11-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='demo')),
            ],
        ),
    ]
