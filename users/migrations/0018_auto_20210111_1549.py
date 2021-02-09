# Generated by Django 3.1.3 on 2021-01-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210109_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(choices=[('Salary', 'Salary'), ('Awards', 'Awards'), ('Grants', 'Grants'), ('Sale', 'Sale'), ('Dividents', 'Dividents'), ('Rental', 'Rental'), ('Refunds', 'Refunds'), ('Coupons', 'Coupons'), ('Lottery', 'Lottery'), ('Capital', 'Capital'), ('Investments', 'Investments'), ('Gift', 'Gift'), ('Others', 'Others')], default='Salary', max_length=11, verbose_name='Category'),
        ),
    ]
