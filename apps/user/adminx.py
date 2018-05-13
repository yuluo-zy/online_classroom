import xadmin

from .models import *
from xadmin import views


class BaseSetting:
    enable_themes = True
    use_booswatch = True

class GlobalSetting:
    site_title = u"慕学在线后台管理系统"
    site_footer = u"墓学在线"
    menu_style = 'accordion'




class EmailVerifyRecordAdmin:
    list_display = ['code', 'email', 'send_type', 'send_date']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_date']



class BannerAdmin:
    list_display = ['title', 'image', 'url', 'index_num', 'add_date']
    search_fields = ['title', 'image', 'url', 'index_num', 'add_date']
    list_filter = ['title', 'image', 'url', 'index_num', 'add_date']





xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)