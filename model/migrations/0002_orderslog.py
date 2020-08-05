# Generated by Django 3.0.6 on 2020-08-05 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Food')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Vendor')),
            ],
        ),
    ]
