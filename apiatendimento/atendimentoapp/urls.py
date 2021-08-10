
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^atendimento/$', views.PedidoList.as_view(), name='pedido-list'),
    url(r'^pedidos/$', views.Pedidos.as_view(), name='pedidos'),

    url(r'^pedido/$', views.ProcedimentosList.as_view(), name='add-pedido'),


]
