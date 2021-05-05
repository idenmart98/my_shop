# Generated by Django 3.2 on 2021-05-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_card_cardproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=300, verbose_name='Имя')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]