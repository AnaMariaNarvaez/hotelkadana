# Generated by Django 3.1.7 on 2021-04-13 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pais', models.CharField(max_length=40)),
                ('Provincia', models.CharField(max_length=70)),
                ('Codigo', models.IntegerField()),
            ],
        ),
    ]