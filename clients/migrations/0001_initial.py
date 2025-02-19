# Generated by Django 4.1.4 on 2022-12-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=50, verbose_name='Familya')),
                ('p_num', models.CharField(max_length=20, verbose_name='Telefon raqami')),
                ('qarz', models.IntegerField(blank=True, default=0, null=True, verbose_name='Qarz')),
            ],
            options={
                'verbose_name': 'Mijoz',
                'verbose_name_plural': 'Mijozlar',
            },
        ),
    ]
