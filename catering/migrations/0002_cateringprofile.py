# Generated by Django 3.2.7 on 2024-03-16 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catering', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CateringProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_Number', models.IntegerField()),
                ('Address', models.CharField(max_length=250)),
                ('Catering_Name', models.CharField(max_length=250)),
                ('Designation', models.CharField(max_length=250)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
