# Generated by Django 2.0.5 on 2019-06-18 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('touch_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('resolution', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('bluetooth', models.CharField(max_length=100)),
                ('cpu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera', models.CharField(max_length=100)),
                ('flashlight', models.CharField(max_length=100)),
                ('phone_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Xiaomi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera', models.CharField(max_length=100)),
                ('phone_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.AddField(
            model_name='apple',
            name='phone_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone'),
        ),
    ]
