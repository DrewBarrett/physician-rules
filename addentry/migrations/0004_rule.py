# Generated by Django 2.0.5 on 2018-05-24 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addentry', '0003_auto_20180524_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of your rule', max_length=256)),
                ('content', models.TextField()),
            ],
        ),
    ]
