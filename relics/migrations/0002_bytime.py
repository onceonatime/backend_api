# Generated by Django 2.1.1 on 2019-07-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ByTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField(default=0)),
                ('clickable', models.BooleanField(null=True)),
            ],
        ),
    ]
