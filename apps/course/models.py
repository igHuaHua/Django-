from django.db import models
from datetime import datetime
from apps.organization.models import CourseOrg

# Create your models here.


class Course(models.Model):
    degree_choices = (
        ('cj', '初级'),
        ('zj', '中级'),
        ('gj', '高级' )
    )
    name = models.CharField('课程名',max_length=50)
    desc = models.CharField('课程描述',max_length=300)
    detail = models.CharField('课程详情',max_length=500)
    degree = models.CharField('难度',choices=degree_choices,max_length=2)
    learn_times = models.IntegerField('学习时长（分钟数）',default=0)
    fav_nums = models.IntegerField('收藏人数',default=0)
    image = models.ImageField('封面图',upload_to='course/%Y%m',max_length=100)
    click_nums = models.IntegerField('点击数',default=0)
    students = models.IntegerField("学习人数", default=0)
    add_time = models.DateTimeField('添加时间',default=datetime.now)
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构", null=True, blank=True)


    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField('章节名',max_length=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的章节 >> {1}'.format(self.course,self.name)


class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name='章节',on_delete=models.CASCADE)
    name = models.CharField('视频名',max_length=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResourse(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField('名称',max_length=100)
    download = models.FileField('资源文件',upload_to='course/resource/%Y/%m',max_length=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name