# Generated by Django 2.2 on 2019-11-14 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('solucionado', models.BooleanField(default=False)),
                ('texto', models.CharField(max_length=512)),
                ('enviadoPor', models.CharField(max_length=36)),
            ],
        ),
    ]
