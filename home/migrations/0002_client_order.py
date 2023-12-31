# Generated by Django 4.2.4 on 2023-08-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('order_frequency', models.IntegerField()),
                ('last_order_at', models.DateTimeField()),
                ('address_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.couriervehicle')),
            ],
        ),
    ]
