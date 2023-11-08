# Copyright 2023 Uladzislau Kakouka
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.addons.portal.controllers.portal import CustomerPortal


class CustomerPortal(CustomerPortal):

    MANDATORY_BILLING_FIELDS = [
        "name",
        "phone",
        "email",
        "street",
        "city",
        "country_id",
        'mobile',
    ]
