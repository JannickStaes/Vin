# Generated by Django 2.2.7 on 2019-11-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('sign', models.CharField(max_length=1)),
                ('currency', models.CharField(max_length=3)),
                ('date', models.DateField()),
                ('account', models.CharField(max_length=16)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
    ]
