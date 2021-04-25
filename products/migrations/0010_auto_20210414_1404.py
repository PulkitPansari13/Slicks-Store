
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_orderitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ['-ordered_at']},
        ),
    ]
