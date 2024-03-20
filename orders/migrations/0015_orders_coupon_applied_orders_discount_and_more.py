# Generated by Django 4.2.3 on 2023-08-22 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0014_coupons'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='coupon_applied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.coupons'),
        ),
        migrations.CreateModel(
            name='Coupon_applied_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.coupons')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]