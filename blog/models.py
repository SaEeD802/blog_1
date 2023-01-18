from django.db import models


# Create your models here.
class Post(models.Model):
    STATUS = (
        ('pub', 'انتشار'),
        ('drf', 'پیش نویس')
    )
    ABOUT = (
        ('غذای سنتی', 'غذای سنتی'),
        ('فست فود', 'فست فود'),
        ('غذای اورگانیک', 'غذای اورگانیک'),
        ('غذای گیاهی', 'غذای گیاهی'),
        ('رژیمی', 'رژیمی'),
        ('غذای بین المللی', 'غذای بین المللی'),
        ('غذای دریایی', 'غذای دریایی'),
        ('پیش غذا', 'پیش غذا'),
        ('نوشیدنی', 'نوشیدنی'),
    )
    title = models.CharField(max_length=150, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='تاریخ تغییر')
    status = models.CharField(choices=STATUS, max_length=15, verbose_name='وضعیت انتشار')
    about = models.CharField(choices=ABOUT, max_length=15, verbose_name='درباره')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='ناشر')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'