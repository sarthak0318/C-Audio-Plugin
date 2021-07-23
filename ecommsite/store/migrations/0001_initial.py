# Generated by Django 3.2.5 on 2021-07-23 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField()),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]
