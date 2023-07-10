from django import template

register = template.Library()

@register.filter
def discounted_price(price, discount):
    if discount is None:
        return price
    else:
        return price - (price * discount / 100)
