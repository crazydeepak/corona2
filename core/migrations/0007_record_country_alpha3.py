# Generated by Django 3.0.4 on 2020-04-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_dump'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='country_alpha3',
            field=models.CharField(default='', max_length=3),
        ),
    ]