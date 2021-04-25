
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210409_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('sm', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL')], max_length=5)),
                ('quant', models.PositiveSmallIntegerField()),
                ('item_price', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.orders')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
            options={
                'unique_together': {('order', 'product', 'size')},
            },
        ),
    ]
