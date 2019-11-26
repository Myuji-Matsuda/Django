from django.db import models
from django.core import validators


class Item(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )
    
    COURSE_CHOICES = (
        (1, '医学部 医学科'),
        (2, '医学部 保健衛生学科 看護学専攻'),
        (3, '医学部 保健衛生学科 検査学専攻'),
        (4, '歯学部 歯学科'),
        (5, '歯学部 口腔衛生学科 口腔保健衛生学専攻'),
        (6, '歯学部 口腔衛生学科 口腔保健工学専攻'),
        (7, 'その他'),
        
    )
    YEAR_CHOICES = (
        (1, '1年生'),
        (2, '2年生'),
        (3, '3年生'),
        (4, '4年生'),
        (5, '5年生'),
        (6, '6年生'),
        (7, 'その他'),
        
    )

    name = models.CharField(
        verbose_name='名前',
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name='年齢',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
    cource = models.IntegerField(
        verbose_name='学科',
        choices=COURSE_CHOICES,
        default=1
    )
    cource = models.IntegerField(
        verbose_name='学年',
        choices=YEAR_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'