# Generated by Django 4.1.5 on 2023-01-18 01:25

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر')),
                ('status', models.CharField(choices=[('pub', 'published'), ('drf', 'draft')], max_length=15, verbose_name='وضعیت انتشار')),
                ('about', models.CharField(choices=[('SONATI', 'sonati'), ('FASTFOOD', 'fastfood'), ('ORGANIC', 'organic'), ('GIAHI', 'giahi'), ('REJIMI', 'rejimi'), ('BINMELALI', 'binmelali'), ('DARYAII', 'daryaii'), ('STARTER', 'starter'), ('DRINK', 'drink')], max_length=15, verbose_name='درباره')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ناشر')),
            ],
        ),
    ]
