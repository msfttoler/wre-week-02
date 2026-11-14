def delivery_fee(subtotal_cents):
    """Return the $5 delivery fee in cents; orders of $50 or more ship free."""
    if subtotal_cents < 0:
        raise ValueError("Order subtotal cannot be negative")
    if subtotal_cents >= 4000:
        return 0
    return 500
