
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210409_0152'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_auto_20210407_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='size',
            field=models.CharField(choices=[('sm', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL')], max_length=5),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_quant', models.PositiveIntegerField()),
                ('total_price', models.PositiveIntegerField()),
                ('shipping_cost', models.PositiveIntegerField()),
                ('payment_status', models.PositiveIntegerField(blank=True, choices=[(1, 'pending'), (2, 'success'), (3, 'failed')], default=1)),
                ('status', models.PositiveIntegerField(blank=True, choices=[(1, 'waiting confirmation'), (2, 'confirmed'), (3, 'processed'), (4, 'shipped'), (5, 'delivered'), (6, 'cancelled')], default=1)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.address')),
                ('user', models.ForeignKey(on_delete=models.SET(products.models.get_sentinel_user), related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
