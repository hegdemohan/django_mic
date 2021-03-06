# Generated by Django 2.1.9 on 2019-06-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('emailId', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('totalRatings', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
