from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_GRAPHICS_THRESHOLD:
        graphics = total * Decimal(settings.STANDARD_GRAPHICS_PERCENTAGE / 100)
        free_graphics_delta = settings.FREE_GRAPHICS_THRESHOLD - total
    else:
        graphics = 0
        free_graphics_delta = 0
    
    grand_total = graphics + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'graphics': graphics,
        'free_graphics_delta': free_graphics_delta,
        'free_graphics_threshold': settings.FREE_GRAPHICS_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
