
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210407_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_quant',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
