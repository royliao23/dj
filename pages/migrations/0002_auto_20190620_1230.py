# Generated by Django 2.2 on 2019-06-20 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='pages.Category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='colour',
            field=models.CharField(choices=[('color', (('white', 'white'), ('blue', 'blue'), ('red', 'red')))], max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='products',
            name='p_code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='p_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='pic',
            field=models.ImageField(max_length=5000, upload_to=''),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(choices=[('Size', (('small', 's'), ('medium', 'm'), ('large', 'l'), ('extr large', 'xl')))], max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='slc',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='products',
            name='sls',
            field=models.CharField(default=(('Size', (('small', 's'), ('medium', 'm'), ('large', 'l'), ('extr large', 'xl'))),), max_length=300),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]