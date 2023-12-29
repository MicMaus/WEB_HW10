# Generated by Django 5.0 on 2023-12-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_author_quote_delete_choice_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='born_date',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]