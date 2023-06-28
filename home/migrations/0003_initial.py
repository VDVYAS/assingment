# Generated by Django 4.2.2 on 2023-06-25 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('company_name', models.TextField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('req_of_shpment', models.CharField(max_length=100)),
                ('tracking_id', models.CharField(max_length=100)),
                ('shipment_size', models.CharField(max_length=100)),
                ('box_count', models.IntegerField(null=True)),
                ('specification', models.CharField(max_length=100)),
                ('checklist_quantity', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
