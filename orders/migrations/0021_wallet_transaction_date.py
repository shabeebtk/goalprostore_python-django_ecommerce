# Generated by Django 4.2.3 on 2023-08-26 06:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_alter_user_wallet_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet_transaction',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]