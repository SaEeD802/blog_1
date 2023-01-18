# Generated by Django 4.1.5 on 2023-01-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='about',
            field=models.CharField(choices=[('غذای سنتی', 'غذای سنتی'), ('فست فود', 'فست فود'), ('غذای اورگانیک', 'غذای اورگانیک'), ('غذای گیاهی', 'غذای گیاهی'), ('رژیمی', 'رژیمی'), ('غذای بین المللی', 'غذای بین المللی'), ('غذای دریایی', 'غذای دریایی'), ('پیش غذا', 'پیش غذا'), ('نوشیدنی', 'نوشیدنی')], max_length=15, verbose_name='درباره'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('pub', 'انتشار'), ('drf', 'پیش نویس')], max_length=15, verbose_name='وضعیت انتشار'),
        ),
    ]