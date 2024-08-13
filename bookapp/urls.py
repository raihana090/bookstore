from django.urls import path
from .import views

urlpatterns = [

    path('createbook',views.creatBook,name='createbook'),

    path('author/',views.Create_Author,name='author'),

    path('',views.listBook,name='booklist'),

    path('detailsview/<int:book_id>/',views.detailsView,name='details'),

    path('updateview/<int:book_id>/',views.updateBook,name='update'),

    path('deleteview/<int:book_id>/',views.deleteView,name='delete'),

    path('base/',views.base),

    path('search/',views.Search_Book,name='search')

]

