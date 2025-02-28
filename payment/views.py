import os
import stripe
import json

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from payment.models import Item, Order
from constants import ERROR_MESSAGE


class ItemListView(ListView):
    model = Item
    template_name = "payment/item_list.html"
    context_object_name = "items"


class ItemRetriveView(DetailView):
    model = Item
    template_name = "payment/item_detail.html"
    context_object_name = "item"


@csrf_exempt
def create_payment(request):
    """
    Создание платежа с помощью stripe
    оплата конкретного товара или товаров из заказа
    """

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            products_pk = data.get("items")
            products = get_list_or_404(Item, pk__in=products_pk)

            currency = products[0].currency
            if any(product.currency != currency for product in products):
                return JsonResponse({"error": ERROR_MESSAGE["currency"]}, status=400)
            total_amount = sum(product.price for product in products)

            if data.get("order_type") == "order":
                order = Order.objects.first()
                if not order:
                    order = Order.objects.create()
                order.items_for_delete = products_pk
                order.save()
                print(order.items_for_delete)

            stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

            intent = stripe.PaymentIntent.create(
                amount=int(total_amount * 100),
                currency=currency,
                automatic_payment_methods={"enabled": True},
            )
            return JsonResponse({"clientSecret": intent["client_secret"]})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=403)


def complete(request):
    try:
        payment_intent_id = request.GET.get("payment_intent")
        client_secret = request.GET.get("payment_intent_client_secret")
        redirect_status = request.GET.get("redirect_status")
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

        context = {
            "payment_intent": payment_intent,
            "client_secret": client_secret,
            "redirect_status": redirect_status,
        }
        return render(request, "payment/complete.html", context)
    except Exception as e:
        print(e)
        return render(request, "pages/400.html", {"error": str(e)})


@csrf_exempt
def add_to_order(request):
    """
    Добавление товара в заказ
    """

    try:
        if request.method == "POST":
            item_id = json.loads(request.body).get("item_id")
            item_obj = get_object_or_404(Item, pk=item_id)

            order = Order.objects.first()
            if not order:
                order = Order.objects.create()
            order.items_for_delete = []
            order.items.add(item_obj)
            order.save()

            return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def order_detail(request):
    order = Order.objects.first()
    return render(request, "payment/order_detail.html", {"order": order})


@csrf_exempt
def remove_from_order(request):
    """
    Удаление товара из заказа
    в случае успешной оплаты
    """

    try:
        if request.method == "POST":
            order = Order.objects.first()
            items_to_delete = order.items_for_delete or []
            items = Item.objects.filter(pk__in=[int(i) for i in items_to_delete])
            order.items.remove(*items)
            order.save()

            return JsonResponse({"success": True})
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e)}, status=400)
