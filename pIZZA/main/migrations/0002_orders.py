# Generated by Django 4.1.7 on 2023-03-15 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uid", models.UUIDField(default=uuid.uuid4)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("processing", "Order Processing"),
                            ("cancelled", "Order Cancelled"),
                            ("out_of_delivery", "Out of Delivery"),
                        ],
                        default="processing",
                        max_length=20,
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("price", models.IntegerField()),
                (
                    "razorpay_order_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "razorpay_payment_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "razorpay_payment_signature",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("product", models.ManyToManyField(to="main.product")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
