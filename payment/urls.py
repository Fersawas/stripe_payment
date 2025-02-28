from django.urls import path, include

from payment.views import (
    ItemListView,
    ItemRetriveView,
    order_detail,
    create_payment,
    complete,
    add_to_order,
    remove_from_order,
)

app_name = "payment"

urlpatterns = [
    path("items/", ItemListView.as_view(), name="items_list"),
    path("items/<int:pk>", ItemRetriveView.as_view(), name="item_detail"),
    path("order/", order_detail, name="order_detail"),
    path("pay/", create_payment, name="create_payment"),
    path("complete/", complete, name="complete"),
    path("add_to_order/", add_to_order, name="add_to_order"),
    path("remove_from_order/", remove_from_order, name="remove_from_order"),
]
