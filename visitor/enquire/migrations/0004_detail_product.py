# Generated by Django 4.2.3 on 2023-07-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquire', '0003_alter_detail_company_name_alter_detail_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='product',
            field=models.CharField(choices=[('I1', 'Item 1'), ('I2', 'Item 2'), ('I3', 'Item 3'), ('I4', 'Item 4'), ('I5', 'Item 5')], default=False, max_length=5),
        ),
    ]
