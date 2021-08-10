
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^atendimento/$', views.PedidoList.as_view(), name='pedido-list'),
    url(r'^pedido/$', views.ProcedimentosList.as_view(), name='add-pedido'),


]
