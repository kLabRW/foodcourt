from django import template
from orders import order

register = template.Library()

@register.inclusion_tag("tags/order_box.html")
def order_box(request):
	order_item_count = order.order_distinct_item_count(request)
	return { 'order_item_count': order_item_count }
