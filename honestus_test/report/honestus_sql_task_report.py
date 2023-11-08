# Copyright 2023 Uladzislau Kakouka
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models, tools


class HonestusSQLTaskReport(models.Model):
    _name = 'honestus.sql.task.report'
    _description = "Honestus Report"
    _rec_name = 'id'
    _auto = False

    id = fields.Integer()
    customer = fields.Many2one('res.partner', string='Customer')
    order_reference = fields.Char(string='Order Reference')
    product_code = fields.Char(string='Product Code')
    honestus_code = fields.Char(string='Honestus Code')
    unit_price = fields.Float(string='Unit Price')
    honestus_price = fields.Float(string='Honestus Price')
    margin = fields.Float(string='Margin')

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE or REPLACE VIEW %s AS (
                SELECT
                    sol.id as id,
                    s.partner_id AS customer,
                    s.name AS order_reference,
                    p.default_code AS product_code,
                    p.honestus_code AS honestus_code,
                    sol.price_unit AS unit_price,
                    p.honestus_price AS honestus_price,
                    (sol.price_unit - prop.value_float) / prop.value_float as margin
                FROM sale_order_line sol
                JOIN sale_order s ON sol.order_id = s.id
                JOIN product_product p ON sol.product_id = p.id
                JOIN ir_property prop on prop.res_id = 'product.product,' || sol.product_id
            ) """ % (self._table,)
        )
