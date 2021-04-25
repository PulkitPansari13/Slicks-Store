
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(1, 'Shirts'), (2, 'Tshirts'), (3, 'Sweatshirts'), (4, 'Jackets'), (5, 'Tanktops'), (6, 'Blazers'), (7, 'Dress'), (8, 'Jeans'), (9, 'Shorts'), (10, 'Track Pants'), (11, 'Trousers')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.ImageField(upload_to=products.models.path_and_rename),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.path_and_rename),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.path_and_rename),
        ),
    ]
