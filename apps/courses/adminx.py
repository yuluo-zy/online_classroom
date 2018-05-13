from .models import *
import xadmin


class CoursesAdmin:

    list_display = ['name', 'doc','degree', 'learn_num', 'save_num',
                    'learn_date', 'clik_num', 'add_time']
    search_fields = ['name', 'doc','degree', 'learn_num', 'save_num',
                    'learn_date', 'clik_num', 'add_time']
    list_filter = ['name', 'doc','degree', 'learn_num', 'save_num',
                    'learn_date', 'clik_num', 'add_time']


class LessonAdmin:
    list_display = ['course', 'lesson_name', 'add_time']
    search_fields = ['course', 'lesson_name', 'add_time']
    list_filter = ['course', 'lesson_name', 'add_time']


class VideoAdmin:
    list_display = ['lesson', 'lesson_name', 'add_time']
    search_fields = ['lesson', 'lesson_name', 'add_time']
    list_filter = ['lesson', 'lesson_name', 'add_time']


class CourseResourceAdmin:

    list_display = ['course', 'name', 'add_time', 'download']
    search_fields = ['course', 'name', 'add_time', 'download']
    list_filter = ['course', 'name', 'add_time', 'download']



xadmin.site.register(Courses,CoursesAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)