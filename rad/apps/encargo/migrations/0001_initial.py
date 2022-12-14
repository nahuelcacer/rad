# Generated by Django 4.1 on 2022-08-26 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Encargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('vehiculo', models.CharField(choices=[('1', 'AUTO'), ('2', 'MOTO'), ('3', 'CAMIONETA')], max_length=1)),
                ('presupuesto', models.CharField(max_length=50)),
                ('personal', models.CharField(choices=[('1', 'NAHUEL'), ('2', 'MAXI')], max_length=1)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='encargo.cliente')),
            ],
        ),
    ]
