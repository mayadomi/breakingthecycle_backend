# Generated by Django 4.2.3 on 2023-09-14 00:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=200)),
                ('anonymous', models.BooleanField(default=False)),
                ('date_donated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=200)),
                ('bio', models.TextField(max_length=500)),
                ('avatar_image', models.URLField(default='https://picsum.photos/200?grayscale')),
                ('background_image', models.URLField(default='https://picsum.photos/1000/160?grayscale')),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('rate', models.PositiveIntegerField(choices=[(1, '1km'), (2, '2km'), (5, '5km')], default=1, help_text='How may kms would you like to ride for each $ donated?')),
                ('kms_ceiling', models.IntegerField(default=400)),
            ],
        ),
        migrations.CreateModel(
            name='RiderUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kms_ridden', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=300)),
                ('image', models.URLField(default='https://picsum.photos/200?grayscale')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='riders.rider')),
            ],
        ),
    ]
