# Generated by Django 3.1.3 on 2020-12-10 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_income_spending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name="Income's Amount"),
        ),
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(choices=[('SLRY', 'Salary'), ('PRFT', 'Profit'), ('ITRT', 'Interest'), ('DVDT', 'Divident'), ('RNTL', 'Rental'), ('CPTL', 'Capital'), ('RYLT', 'Royalty'), ('GIFT', 'Gift'), ('OTRS', 'Others')], default='SLRY', max_length=4, verbose_name="Income's Category"),
        ),
        migrations.AlterField(
            model_name='income',
            name='name',
            field=models.CharField(max_length=50, verbose_name="Income's Name"),
        ),
        migrations.AlterField(
            model_name='income',
            name='recurrent',
            field=models.BooleanField(default=False, verbose_name='Recurrent Income'),
        ),
        migrations.AlterField(
            model_name='spending',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name="Spending's Amount"),
        ),
        migrations.AlterField(
            model_name='spending',
            name='category',
            field=models.CharField(choices=[('UTLT', 'Utilities'), ('RENT', 'Rent'), ('INVC', 'Invoices'), ('SHPG', 'Shopping'), ('FOOD', 'Food'), ('EDCN', 'Education'), ('FUN', 'Fun'), ('INVT', 'Investment'), ('OTRS', 'Others')], default='UTLT', max_length=4, verbose_name="Spending's Category"),
        ),
        migrations.AlterField(
            model_name='spending',
            name='name',
            field=models.CharField(max_length=50, verbose_name="Spending's Name"),
        ),
        migrations.AlterField(
            model_name='spending',
            name='recurrent',
            field=models.BooleanField(default=False, verbose_name='Recurrent Spending'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name="User's Avatar")),
                ('currency', models.CharField(choices=[('AED', 'Aed'), ('AUD', 'Aud'), ('BRL', 'Brl'), ('CAD', 'Cad'), ('CHF', 'Chf'), ('CLP', 'Clp'), ('CNY', 'Cny'), ('COP', 'Cop'), ('CZK', 'Czk'), ('DKK', 'Dkk'), ('EUR', 'Eur'), ('GBP', 'Gbp'), ('HKD', 'Hkd'), ('HUF', 'Huf'), ('IDR', 'Idr'), ('ILS', 'Ils'), ('INR', 'Inr'), ('JPY', 'Jpy'), ('KRW', 'Krw'), ('MDL', 'Mdl'), ('MXN', 'Mxn'), ('MYR', 'Myr'), ('NOK', 'Nok'), ('NZD', 'Nzd'), ('PHP', 'Php'), ('PLN', 'Pln'), ('RON', 'Ron'), ('RUB', 'Rub'), ('SAR', 'Sar'), ('SEK', 'Sek'), ('SGD', 'Sgd'), ('THB', 'Thb'), ('TRY', 'Try'), ('TWD', 'Twd'), ('USD', 'Usd'), ('ZAR', 'Zar')], default='USD', max_length=3, verbose_name="User's Profile Currency")),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
