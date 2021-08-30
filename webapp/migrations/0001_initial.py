# Generated by Django 3.2.5 on 2021-08-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=20, null=True)),
                ('description', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=50)),
            ],
        ),
    ]
