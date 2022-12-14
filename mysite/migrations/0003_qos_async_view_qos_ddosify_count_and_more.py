# Generated by Django 4.0.8 on 2022-12-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_remove_qos_async_view_remove_qos_ddosify_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qos',
            name='async_view',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='qos',
            name='ddosify_count',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='qos',
            name='ddosify_duration',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='qos',
            name='ddosify_timeout',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='qos',
            name='ping_algorithm',
            field=models.CharField(default='binary_search', max_length=13),
        ),
    ]
