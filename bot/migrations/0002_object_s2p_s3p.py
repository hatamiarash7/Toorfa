# Generated by Django 2.0 on 2017-12-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50, null=True)),
                ('material', models.CharField(max_length=50, null=True)),
                ('size_x', models.IntegerField(null=True)),
                ('size_y', models.IntegerField(null=True)),
                ('size_z', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('volume', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('status', models.IntegerField(null=True)),
                ('created_date', models.CharField(max_length=50, null=True)),
                ('created_time', models.CharField(max_length=50, null=True)),
                ('created_place', models.CharField(max_length=50, null=True)),
                ('temp_status', models.CharField(max_length=100, null=True)),
                ('temp_degree', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='S2P',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NP', models.CharField(max_length=100, null=True)),
                ('VP', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='S3P',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NP', models.CharField(max_length=100, null=True)),
                ('VP', models.CharField(max_length=100, null=True)),
                ('ADJP', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
