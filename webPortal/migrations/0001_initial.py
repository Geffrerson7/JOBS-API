# Generated by Django 4.2 on 2023-05-05 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPortal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('prefixe', models.CharField(default='', max_length=200)),
                ('logo', models.URLField(max_length=500)),
                ('url', models.URLField()),
            ],
            options={
                'db_table': 'Web_Portal',
            },
        ),
    ]
