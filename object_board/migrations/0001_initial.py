# Generated by Django 2.2.4 on 2019-08-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.TextField()),
                ('name', models.TextField()),
                ('standard', models.TextField()),
                ('kcal', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='METs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.TextField()),
                ('name', models.TextField()),
                ('mets', models.TextField()),
            ],
        ),
    ]
