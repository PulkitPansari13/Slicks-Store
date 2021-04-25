
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cart_cartitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='quant',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
