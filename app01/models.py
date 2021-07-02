from django.db import models
class Aliyun_list(models.Model):
    name = models.CharField(max_length=60, verbose_name="云名称", null=True)
    login = models.URLField(max_length=60, verbose_name="登录地址", null=True)
    type = models.CharField(max_length=60, verbose_name="备注", null=True)
    phone = models.CharField(max_length=11, verbose_name="绑定手机", null=True)
    account_number = models.CharField(max_length=30, verbose_name="账号", null=True)
    password = models.CharField(max_length=30, verbose_name="密码", null=True)
    class Meta:
        verbose_name = "阿里云账号密码"


from django.db import models
# Create your models here.
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    class Meta:
        verbose_name = '添加'

class Cat_Content(models.Model):
    class Meta:
        verbose_name = '查看'