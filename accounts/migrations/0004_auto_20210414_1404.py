
import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210409_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phno',
            field=models.CharField(max_length=10, null=True, validators=[accounts.models.phone_validator]),
        ),
    ]
