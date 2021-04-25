
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20210403_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('network', 'Network'), ('mufti', 'Mufti'), ('anthem', 'Anthem'), ('blue saint', 'Blue Saint'), ('dennis lingo', 'Dennis Lingo'), ('balista', 'Balista'), ('hue', 'Hue'), ('harbour', 'Harbour'), ('flyrs', 'Flyrs'), ('up', 'UP')], max_length=70),
        ),
        migrations.AlterField(
            model_name='product',
            name='composition',
            field=models.CharField(default='100% Cotton', max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=products.models.get_fake_description),
        ),
        migrations.AlterField(
            model_name='product',
            name='l_quant',
            field=models.PositiveIntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='m_quant',
            field=models.PositiveIntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='sm_quant',
            field=models.PositiveIntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='xl_quant',
            field=models.PositiveIntegerField(default=15),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'product')},
            },
        ),
    ]
