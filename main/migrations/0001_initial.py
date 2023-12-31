# Generated by Django 4.2.5 on 2023-09-06 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ward',
            fields=[
                ('ward_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=20, null=True)),
                ('number_beds', models.IntegerField(default=5, null=True)),
                ('nurse_in_charge', models.CharField(max_length=25, null=True)),
                ('ward_type', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('patient_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('initials', models.CharField(max_length=3, null=True)),
                ('sex', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=30, null=True)),
                ('post_card', models.CharField(max_length=6, null=True)),
                ('admission', models.DateField(null=True)),
                ('DOB', models.DateField()),
                ('next_of_kin', models.CharField(max_length=30, null=True)),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ward')),
            ],
        ),
    ]
