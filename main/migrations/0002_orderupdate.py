# Generated by Django 3.0.1 on 2020-01-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.ImageField(default='', upload_to='')),
                ('update_desc', models.CharField(max_length=1000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
