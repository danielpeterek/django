# Generated by Django 3.2 on 2021-04-19 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0003_auto_20210419_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='druh',
            options={'ordering': ['oznaceni_druhu'], 'verbose_name': 'Druh zboží', 'verbose_name_plural': 'Druh zboží'},
        ),
        migrations.AlterModelOptions(
            name='zbozi',
            options={'ordering': ['-cena', 'nazev'], 'verbose_name': 'Zboží', 'verbose_name_plural': 'Zboží'},
        ),
    ]
