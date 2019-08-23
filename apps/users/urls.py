from django.urls import path,re_path
from apps.users.views import ForgetPwdView,Login,RegisterView,index,ActiveUserView,ResetView,ModifyPwdView
import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('login/' ,Login.as_view(), name='login'),
    path('index/', index, name='index'),
    path('register/', RegisterView.as_view(),name='register'),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(),name='user_active'),
    path('forget/', ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
]
