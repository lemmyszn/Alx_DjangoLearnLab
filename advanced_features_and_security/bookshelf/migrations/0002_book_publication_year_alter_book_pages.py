# Generated by Django 5.0.7 on 2024-08-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.PositiveIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(),
        ),
    ]
