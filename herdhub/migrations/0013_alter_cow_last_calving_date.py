# Generated by Django 5.1 on 2024-09-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herdhub', '0012_alter_bull_registration_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cow',
            name='last_calving_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
