# Generated by Django 3.2 on 2021-04-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_card_cardproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AddField(
            model_name='cardproduct',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]