# Generated by Django 4.0.8 on 2022-12-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QoS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_url', models.CharField(max_length=120)),
                ('ping_count', models.IntegerField(default=5)),
                ('ping_timeout', models.DecimalField(decimal_places=2, default=0.2, max_digits=3)),
                ('ping_algorithm', models.CharField(default='binary_search', max_length=13)),
                ('ddosify_count', models.IntegerField(default=100)),
                ('ddosify_duration', models.IntegerField(default=5)),
                ('ddosify_timeout', models.IntegerField(default=1)),
                ('async_view', models.BooleanField(default=True)),
            ],
        ),
    ]
