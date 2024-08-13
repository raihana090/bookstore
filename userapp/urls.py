from django.urls import path

from.import views

urlpatterns=[

    path('',views.listBook,name='book-list'),
    path('details/<int:book_id>/',views.detailsView,name='userdetails'),
    path('search-user/',views.Search_Book,name='usersearch'),
    path('add_to_cart/<int:book_id>/',views.add_to_cart,name='add_to_cart'),
    path('view-cart/',views.ViewCart,name='viewcart'),
    path('increase/<int:item_id>/',views.increase_quantity,name='increase_quantity'),
    path('decrease/<int:item_id>/',views.decrease_quantity,name='decrease_quantity'),
    path('remove-from-cart/<int:item_id>/',views.remove_from_cart,name='remove_cart'),
    path('create-checkout-session/',views.create_checkout_session,name='create-checkout-session'),
    path('success/',views.success,name='success'),
    path('cancel/',views.cancel,name='cancel')

]
