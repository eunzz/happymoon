# Generated by Django 2.0.7 on 2018-08-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='recipient_add_detail',
            field=models.CharField(default='', max_length=100, verbose_name='상세주소'),
            preserve_default=False,
        ),
    ]
