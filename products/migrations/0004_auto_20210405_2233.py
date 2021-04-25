
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210405_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='l_quant',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='m_quant',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='sm_quant',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='xl_quant',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
