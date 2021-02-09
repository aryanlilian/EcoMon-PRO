# Generated by Django 3.1.3 on 2020-12-10 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name="User's Avatar")),
                ('currency', models.CharField(choices=[('AED', 'Aed'), ('AUD', 'Aud'), ('BRL', 'Brl'), ('CAD', 'Cad'), ('CHF', 'Chf'), ('CLP', 'Clp'), ('CNY', 'Cny'), ('COP', 'Cop'), ('CZK', 'Czk'), ('DKK', 'Dkk'), ('EUR', 'Eur'), ('GBP', 'Gbp'), ('HKD', 'Hkd'), ('HUF', 'Huf'), ('IDR', 'Idr'), ('ILS', 'Ils'), ('INR', 'Inr'), ('JPY', 'Jpy'), ('KRW', 'Krw'), ('MDL', 'Mdl'), ('MXN', 'Mxn'), ('MYR', 'Myr'), ('NOK', 'Nok'), ('NZD', 'Nzd'), ('PHP', 'Php'), ('PLN', 'Pln'), ('RON', 'Ron'), ('RUB', 'Rub'), ('SAR', 'Sar'), ('SEK', 'Sek'), ('SGD', 'Sgd'), ('THB', 'Thb'), ('TRY', 'Try'), ('TWD', 'Twd'), ('USD', 'Usd'), ('ZAR', 'Zar')], default='USD', max_length=3, verbose_name="User's Profile Currency")),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]