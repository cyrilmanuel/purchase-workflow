# Copyright 2023 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import TransactionCase


class TestPurchaseTotalOrderedQty(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create({"name": "Purchase Partner"})
        cls.product = cls.env["product.product"].create(
            # Use "service" type product to be able to set receipt qty manually
            {"name": "Purchase Product", "type": "service"}
        )
        cls.order = cls.env["purchase.order"].create(
            {
                "partner_id": cls.partner.id,
                "company_id": cls.env.user.company_id.id,
            }
        )

    def test_00_order_empty_without_lines(self):
        """Test empty order w/o lines: receipt percentage should be 100%"""
        self.assertEqual(self.order.receipt_percentage, 100)
        self.assertEqual(self.order.receipt_percentage_display, 1)

    def test_01_order_empty_with_lines(self):
        """Test empty order w/ lines: receipt percentage should be 100%"""
        self.env["purchase.order.line"].create(
            {
                "order_id": self.order.id,
                "name": self.product.name,
                "product_id": self.product.id,
                "product_qty": 0.0,
            }
        )
        self.assertEqual(self.order.order_line.receipt_percentage, 100)
        self.assertEqual(self.order.receipt_percentage, 100)
        self.assertEqual(self.order.receipt_percentage_display, 1)

    def test_02_order_with_lines(self):
        """Test order w/ lines

        Add 1 completely received lines, and 1 half-received lines: receipt %
        should be 75.0%
        """
        self.env["purchase.order.line"].create(
            [
                {
                    "order_id": self.order.id,
                    "name": self.product.name,
                    "product_id": self.product.id,
                    "product_qty": 10.0,
                    "qty_received_manual": 10.0,
                },
                {
                    "order_id": self.order.id,
                    "name": self.product.name,
                    "product_id": self.product.id,
                    "product_qty": 5.0,
                    "qty_received_manual": 2.5,
                },
            ]
        )
        self.assertEqual(self.order.order_line[0].receipt_percentage, 100)
        self.assertEqual(self.order.order_line[1].receipt_percentage, 50)
        self.assertEqual(self.order.receipt_percentage, 75)
        self.assertEqual(self.order.receipt_percentage_display, 0.75)
