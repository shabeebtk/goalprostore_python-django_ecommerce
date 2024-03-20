# Generated by Django 4.2.3 on 2023-08-14 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_alter_orders_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('landmark', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]