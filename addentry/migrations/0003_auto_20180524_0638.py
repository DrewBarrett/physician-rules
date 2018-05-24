# Generated by Django 2.0.5 on 2018-05-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addentry', '0002_auto_20180522_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='physician',
            name='age_results',
            field=models.CharField(blank=True, default='No output, check your rules or re-run them by using the button', editable=False, max_length=256),
        ),
        migrations.AddField(
            model_name='physician',
            name='board_results',
            field=models.CharField(blank=True, default='No output, check your rules or re-run them by using the button', editable=False, max_length=256),
        ),
        migrations.AddField(
            model_name='physician',
            name='language_results',
            field=models.CharField(blank=True, default='No output, check your rules or re-run them by using the button', editable=False, max_length=256),
        ),
        migrations.AddField(
            model_name='physician',
            name='location_results',
            field=models.CharField(blank=True, default='No output, check your rules or re-run them by using the button', editable=False, max_length=256),
        ),
        migrations.AddField(
            model_name='physician',
            name='npi_results',
            field=models.CharField(blank=True, default='No output, check your rules or re-run them by using the button', editable=False, max_length=256),
        ),
        migrations.AddField(
            model_name='physician',
            name='rating_results',
            field=models.CharField(blank=True, default='No output, check your rules or re-run them by using the button', editable=False, max_length=256),
        ),
    ]
