# Generated by Django 3.0.6 on 2020-06-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200602_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cannedfood',
            name='note',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
