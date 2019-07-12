# Generated by Django 2.1.10 on 2019-07-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccbaKdcd', models.IntegerField(default=0)),
                ('ccbaAsno', models.CharField(blank=True, max_length=20, null=True)),
                ('ccbaCtcd', models.CharField(default=0, max_length=3)),
                ('ccbaPcd1', models.CharField(default=0, max_length=3)),
                ('ccbaMnm1', models.CharField(blank=True, max_length=20, null=True)),
                ('ccbaMnm2', models.CharField(blank=True, max_length=20, null=True)),
                ('ccmaName', models.CharField(blank=True, max_length=20, null=True)),
                ('ccbaCtcdNm', models.CharField(blank=True, max_length=20, null=True)),
                ('ccsiName', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=30, null=True)),
                ('latitude', models.CharField(blank=True, max_length=30, null=True)),
                ('ccbaLcad', models.TextField(default='-')),
                ('content', models.TextField(default='-')),
            ],
        ),
    ]