# Generated by Django 4.2 on 2024-07-02 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('League', '0002_lliga_temporada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lliga',
            name='any_fundacio',
        ),
    ]