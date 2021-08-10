
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^atendimentos/$', views.AtendimentoList.as_view(), name='atendimento-list'),

]
