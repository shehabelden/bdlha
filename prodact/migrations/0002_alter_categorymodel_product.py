# Generated by Django 4.1 on 2023-01-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='prodact.productmodel'),
        ),
    ]
