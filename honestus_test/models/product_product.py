# Copyright 2023 Uladzislau Kakouka
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    honestus_code = fields.Char(string='Honestus Code')
    honestus_price = fields.Float(string='Honestus Price')
