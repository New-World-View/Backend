# Generated by Django 5.1.6 on 2025-02-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=110)),
                ('message', models.TextField(max_length=355)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
