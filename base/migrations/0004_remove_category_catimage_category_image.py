# Generated by Django 4.0.2 on 2022-05-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='catimage',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
    ]