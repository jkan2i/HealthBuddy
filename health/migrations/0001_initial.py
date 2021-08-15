# Generated by Django 3.1.4 on 2020-12-14 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.CharField(max_length=10, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('timing', models.CharField(max_length=10, null=True)),
                ('days_time', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('specialist', models.CharField(max_length=100, null=True)),
                ('clinic', models.CharField(max_length=100, null=True)),
                ('cl_address', models.CharField(max_length=100, null=True)),
                ('daystiming', models.CharField(max_length=100, null=True)),
                ('timing', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('biography', models.TextField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
