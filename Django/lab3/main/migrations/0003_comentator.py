# Generated by Django 3.2.8 on 2021-11-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_costomer'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('comment', models.CharField(max_length=200)),
                ('datepub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]