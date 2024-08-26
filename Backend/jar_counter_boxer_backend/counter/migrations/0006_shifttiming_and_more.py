# Generated by Django 4.2.13 on 2024-07-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0005_remove_jarcount_inventory_delete_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftTiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift1_start', models.TimeField(default='08:00')),
                ('shift2_start', models.TimeField(default='20:00')),
            ],
        ),
        migrations.RemoveIndex(
            model_name='jarcount',
            name='counter_jar_shift_ba3f88_idx',
        ),
        migrations.RemoveField(
            model_name='jarcount',
            name='shift',
        ),
        migrations.AddField(
            model_name='jarcount',
            name='shift1_start',
            field=models.TimeField(default='08:00'),
        ),
        migrations.AddField(
            model_name='jarcount',
            name='shift2_start',
            field=models.TimeField(default='20:00'),
        ),
    ]
