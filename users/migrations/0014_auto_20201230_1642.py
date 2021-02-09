# Generated by Django 3.1.3 on 2020-12-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20201230_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(choices=[('SLRY', 'Salary'), ('PRFT', 'Profit'), ('ITRT', 'Interest'), ('DVDT', 'Divident'), ('RNTL', 'Rental'), ('CPTL', 'Capital'), ('RYLT', 'Royalty'), ('GIFT', 'Gift'), ('OTHR', 'Others')], default='SLRY', max_length=4, verbose_name='Category'),
        ),
    ]
