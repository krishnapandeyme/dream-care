# Generated by Django 2.2 on 2020-10-16 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_inactive', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_inactive', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.ServiceCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProviderServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.ServiceCategory')),
                ('service_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.ServiceSubCategory')),
            ],
        ),
    ]
