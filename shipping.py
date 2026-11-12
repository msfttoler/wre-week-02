def delivery_fee(subtotal_cents):
    """Return the delivery fee in integer cents."""
    if subtotal_cents < 0:
        raise ValueError("Order subtotal cannot be negative")
    if subtotal_cents >= 5000:
        return 0
    return 500
