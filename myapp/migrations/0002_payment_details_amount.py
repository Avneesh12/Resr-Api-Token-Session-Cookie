# Generated by Django 4.0.2 on 2022-04-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_details',
            name='amount',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]