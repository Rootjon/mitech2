# Generated by Django 3.2.9 on 2021-11-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techit', '0002_demo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='expert')),
                ('social_facebook', models.URLField()),
                ('social_github', models.URLField()),
            ],
        ),
    ]
