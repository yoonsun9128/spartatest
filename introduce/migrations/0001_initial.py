# Generated by Django 4.1.1 on 2022-09-28 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accesslogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='접속 시간')),
                ('location', models.CharField(max_length=50, verbose_name='접속 경로')),
            ],
        ),
    ]
