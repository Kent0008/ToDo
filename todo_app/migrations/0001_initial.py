# Generated by Django 4.2.1 on 2023-05-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('description', models.TextField(verbose_name='Описания')),
                ('create_data', models.DateTimeField(auto_now_add=True)),
                ('update_data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]



