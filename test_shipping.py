import unittest

from shipping import delivery_fee


class DeliveryFeeTests(unittest.TestCase):
    def test_order_below_fifty_dollars_has_delivery_fee(self):
        self.assertEqual(delivery_fee(4900), 500)

    def test_order_at_fifty_dollars_ships_free(self):
        self.assertEqual(delivery_fee(5000), 0)

    def test_order_above_fifty_dollars_ships_free(self):
        self.assertEqual(delivery_fee(7500), 0)

    def test_negative_order_is_rejected(self):
        with self.assertRaises(ValueError):
            delivery_fee(-1)


if __name__ == "__main__":
    unittest.main()
