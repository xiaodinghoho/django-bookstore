# Generated by Django 2.0.4 on 2018-05-16 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodslist', '0002_goods_goodsauthoe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='goodsAuthoe',
            new_name='goodsAuthor',
        ),
    ]
