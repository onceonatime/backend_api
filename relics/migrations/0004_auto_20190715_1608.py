# Generated by Django 2.1.1 on 2019-07-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relics', '0003_auto_20190715_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bytime',
            name='ccbaAsno',
        ),
        migrations.RemoveField(
            model_name='bytime',
            name='ccbaCtcd',
        ),
        migrations.RemoveField(
            model_name='bytime',
            name='ccbaKdcd',
        ),
        migrations.AddField(
            model_name='bytime',
            name='incidents',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
