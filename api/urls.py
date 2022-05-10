from django.urls import path
from .views import BookApiListView, UserApiListView, BookApiDestroyView, BookApiCreateView,\
                    BookApiRetrieveView, BookApiUpdateView


urlpatterns = [
    path('booklist/', BookApiListView.as_view(), name = 'apibooklist'),
    path('bookcreate/', BookApiCreateView.as_view(), name = 'apibookcreate'),
    path('bookretrieve/<int:pk>', BookApiRetrieveView.as_view(), name = 'apibookretrieve'),
    path('bookupdate/<int:pk>', BookApiUpdateView.as_view(), name = 'apibookupdate'),
    path('bookdestroy/<int:pk>', BookApiDestroyView.as_view(), name = 'apibookdestroy'),
    path('userlist/', UserApiListView.as_view(), name = 'apiuserlist'),
]
