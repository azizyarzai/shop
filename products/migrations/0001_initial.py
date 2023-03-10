# Generated by Django 4.1.5 on 2023-02-25 13:15

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'null': 'please fill the input', 'unique': 'No Duplicates.'}, help_text='Please enter a unique value.', max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('price', models.IntegerField(validators=[products.models.price_gt_500])),
                ('is_available', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.file, validators=[products.models.image_validator])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.category')),
            ],
            options={
                'db_table': 'product',
            },
            managers=[
                ('db', django.db.models.manager.Manager()),
            ],
        ),
    ]
