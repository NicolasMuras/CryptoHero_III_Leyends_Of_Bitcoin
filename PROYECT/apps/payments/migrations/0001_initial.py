# Generated by Django 3.1.6 on 2021-02-13 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Direccion')),
                ('city', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('state', models.CharField(max_length=100, verbose_name='Estado')),
                ('x_coord', models.FloatField()),
                ('y_coord', models.FloatField()),
            ],
            options={
                'verbose_name': 'Coordinates',
                'verbose_name_plural': 'Coordinates',
            },
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('quantity', models.FloatField()),
                ('cryptocurrency', models.CharField(max_length=50, verbose_name='Criptodivisa')),
                ('wallet_address', models.CharField(max_length=32, verbose_name='Wallet')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.location', verbose_name='Coordenadas')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
    ]