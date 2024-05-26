# Generated by Django 5.0.3 on 2024-04-19 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_title', models.CharField(max_length=85)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.task')),
            ],
        ),
    ]
