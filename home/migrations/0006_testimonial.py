# Generated by Django 3.1.3 on 2020-12-26 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201226_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('person_type', models.CharField(choices=[('CLNT', 'Client'), ('PCLT', 'Pro Client'), ('STFF', 'Stuff')], default='CLNT', max_length=4, verbose_name='Person Type')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date/Time')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date/Time')),
            ],
        ),
    ]