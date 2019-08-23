from django.db import models
from datetime import datetime
from apps.users.models import UserProfile
from apps.course.models import Course
# Create your models here.


class UserAsk(models.Model):
    name = models.CharField('姓名',max_length=20)
    mobile = models.IntegerField('手机号')
    course_name = models.CharField('课程名',max_length=50)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserMessage(models.Model):
    # user字段，默认0代表消息是发送给所有用户，而不是某个单独用户；可以通过user.id发送给特定用户消息
    user = models.IntegerField('接收用户',default=0)
    message = models.CharField('消息内容',max_length=500)
    has_read = models.BooleanField('是否已读',default=False)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间',default=datetime.now)
    comments = models.CharField('评论',default='', max_length=200)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    FAV_TYPE = (
        (1,'课程'),
        (2,'课程机构'),
        (3,'讲师'),
    )

    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    fav_id = models.IntegerField('数据id', default=0)
    fav_type = models.IntegerField(verbose_name='收藏类型', choices=FAV_TYPE, default=1)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name