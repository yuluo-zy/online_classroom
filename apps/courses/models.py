from datetime import datetime

from django.db import models

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"课程名称")
    doc = models.CharField(max_length=300,verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(verbose_name="等级", max_length=10,choices=(("rb",u"初级"), ("zj",u"中级"), ("gj",u"高级")),)
    learn_num = models.IntegerField(default=0, verbose_name=u"学习人数")
    save_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    learn_date = models.IntegerField(default=0,verbose_name=u"学习时长")
    image = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面", max_length=100)
    clik_num = models.IntegerField(default=0,verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}--({1})'.format(self.name, self.doc)

class Lesson(models.Model):
    course = models.ForeignKey(Courses,verbose_name=u"课程名", on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=30,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节目录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}--({1})'.format(self.course, self.lesson_name)


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节名", on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=30, verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频目录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}--({1})'.format(self.lesson_name, self.lesson)

class CourseResource(models.Model):
    course = models.ForeignKey(Courses,verbose_name=u"课程", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u"下载")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}--({1})'.format(self.course, self.add_time, )
