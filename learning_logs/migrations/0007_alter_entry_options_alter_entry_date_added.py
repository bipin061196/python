# Generated by Django 4.2.8 on 2023-12-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
