# Generated by Django 3.2.3 on 2021-11-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombreUsuario', models.CharField(max_length=50)),
                ('correoUsuario', models.CharField(max_length=50)),
                ('claveUsuario', models.CharField(max_length=50)),
            ],
        ),
    ]
