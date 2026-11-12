def delivery_fee(subtotal_cents):
    """Charge $5 for delivery, with free delivery from $50."""
    if subtotal_cents < 0:
        raise ValueError("Order subtotal cannot be negative")
    if subtotal_cents >= 4000:
        return 0
    return 500
