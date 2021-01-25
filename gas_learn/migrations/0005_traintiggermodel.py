# Generated by Django 3.1.5 on 2021-01-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_learn', '0004_auto_20210125_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainTiggerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epoch', models.IntegerField()),
                ('isOk', models.BooleanField()),
            ],
            options={
                'verbose_name': 'TrainTiggerModel',
                'verbose_name_plural': 'TrainTiggerModels',
                'db_table': 'TrainTigger',
                'managed': True,
            },
        ),
    ]