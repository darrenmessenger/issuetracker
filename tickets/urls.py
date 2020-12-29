from django.conf.urls import url
from .views import get_tickets, ticket_detail, create_or_edit_ticket, ticket_vote, ticket_vote_list

urlpatterns = [
    url(r'^$', get_tickets, name='get_tickets'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name = 'ticket_detail'),
    url(r'^(?P<pk>\d+)/$', ticket_vote, name = 'ticket_vote'),
    url(r'^tickets/(?P<pk>[0-9]+)/like/$', ticket_vote_list, name='ticket_vote_list'),
    url(r'^ticket/(?P<pk>[0-9]+)/like/$', ticket_vote, name='ticket_vote'),
    url(r'^new/$', create_or_edit_ticket, name = 'new_ticket'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name = 'edit_ticket')
]