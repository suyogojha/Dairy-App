# Generated by Django 3.0.5 on 2020-09-29 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MilkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animalname', models.CharField(choices=[('Cow', 'Cow'), ('Buffaloe', 'Buffalo'), ('Others', 'Others')], max_length=200)),
                ('milkprice', models.FloatField(db_index=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('managername', models.CharField(max_length=200)),
                ('vendorname', models.CharField(db_index=True, max_length=200, unique=True)),
                ('joiningdate', models.DateField(auto_now_add=True)),
                ('address', models.CharField(db_index=True, max_length=200)),
                ('vendorcontact', models.CharField(db_index=True, max_length=14)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='vendorledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(db_index=True, max_length=1000000)),
                ('price', models.FloatField(db_index=True, default=0.0, max_length=1000000)),
                ('quantity', models.FloatField(db_index=True, default=0.0, max_length=1000000)),
                ('total', models.FloatField(db_index=True, default=0.0, max_length=1000000)),
                ('related_milkcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendorledger', to='dairyapp.MilkCategory')),
                ('related_vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendorledger', to='dairyapp.Vendor')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Customer', 'Customer'), ('Manager', 'Manager')], max_length=20, null=True)),
                ('contact_number', models.CharField(max_length=20, null=True, unique=True)),
                ('joining_data', models.DateField()),
                ('address', models.CharField(max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-user_type',),
            },
        ),
        migrations.AddField(
            model_name='milkcategory',
            name='related_vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MilkCategory', to='dairyapp.Vendor'),
        ),
        migrations.CreateModel(
            name='CustomerMilkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animalname', models.CharField(choices=[('Cow', 'Cow'), ('Buffaloe', 'Buffalo'), ('Others', 'Others')], max_length=200)),
                ('milkprice', models.FloatField(db_index=True, max_length=200)),
                ('related_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CustomerMilkCategory', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customerledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(db_index=True, max_length=1000000)),
                ('price', models.FloatField(db_index=True, default=0.0, max_length=1000000)),
                ('quantity', models.FloatField(db_index=True, default=0.0, max_length=1000000)),
                ('total', models.FloatField(db_index=True, default=0.0, max_length=1000000)),
                ('related_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Customerledger', to=settings.AUTH_USER_MODEL)),
                ('related_milk_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Customerledger', to='dairyapp.CustomerMilkCategory')),
            ],
        ),
    ]
