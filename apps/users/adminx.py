import xadmin
from .models import EmailVerifyRecord,Banner
from xadmin import views

# 创建xadmin的最基本管理器配置，并与view绑定


class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 将基本配置管理与view绑定


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']


class GlobalSettings(object):
    # 修改title
    site_title = '我爱学习'
    # 修改footer
    site_footer = '天天学习'
    # 收起菜单
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)

