# Generated by Django 2.2.5 on 2019-09-15 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='상품명')),
                ('price', models.IntegerField(verbose_name='상품가격')),
                ('description', models.TextField(verbose_name='상품설명')),
                ('stuck', models.IntegerField(verbose_name='재고')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
            ],
            options={
                'verbose_name': '제품',
                'verbose_name_plural': '제품',
                'db_table': 'fc_product',
            },
        ),
    ]
