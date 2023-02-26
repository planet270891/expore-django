# Generated by Django 3.2.8 on 2022-04-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('email', models.CharField(max_length=191, null=True)),
                ('phone', models.CharField(max_length=191, null=True)),
                ('website', models.CharField(max_length=191, null=True)),
                ('street_address', models.TextField(null=True)),
                ('date_joined', models.DateField(null=True)),
            ],
            options={
                'db_table': 'ref_contacts',
            },
        ),
    ]
