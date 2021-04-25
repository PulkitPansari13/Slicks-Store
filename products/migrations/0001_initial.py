
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uqid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('brand', models.CharField(max_length=70)),
                ('name', models.CharField(max_length=150)),
                ('img1', models.ImageField(upload_to='img/prod')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='img/prod')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='img/prod')),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('shirts', 'Shirts'), ('tshirts', 'Tshirts'), ('sweatshirts', 'Sweatshirts'), ('jackets', 'Jackets'), ('tanktops', 'Tanktops'), ('blazers', 'Blazers'), ('dress', 'Dress'), ('jeans', 'Jeans'), ('shorts', 'Shorts'), ('trackpants', 'Track Pants'), ('trousers', 'Trousers')], max_length=25)),
                ('composition', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=15)),
                ('sm_quant', models.PositiveIntegerField()),
                ('m_quant', models.PositiveIntegerField()),
                ('l_quant', models.PositiveIntegerField()),
                ('xl_quant', models.PositiveIntegerField()),
            ],
        ),
    ]
