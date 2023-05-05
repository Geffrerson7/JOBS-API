# Generated by Django 4.2 on 2023-05-05 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webPortal', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=500)),
                ('company', models.CharField(max_length=200)),
                ('modality', models.CharField(max_length=200)),
                ('applicationDate', models.DateField(auto_now_add=True)),
                ('publicationDate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('webPortal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webPortal', to='webPortal.webportal')),
            ],
            options={
                'db_table': 'Job',
            },
        ),
    ]
