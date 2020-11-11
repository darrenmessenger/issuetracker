from django.conf.urls import url
from .views import get_tickets, ticket_detail, create_or_edit_ticket

urlpatterns = [
    url(r'^$', get_tickets, name='get_tickets'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name = 'ticket_detail'),
    url(r'^new/$', create_or_edit_ticket, name = 'new_ticket'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name = 'edit_ticket')
]