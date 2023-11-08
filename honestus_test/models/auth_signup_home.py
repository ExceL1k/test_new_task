# Copyright 2023 Uladzislau Kakouka
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request


class AuthSignupHome(AuthSignupHome):

    def _prepare_signup_values(self, qcontext):
        values = super()._prepare_signup_values(qcontext)
        mobile = request.params.get('mobile', False)
        if mobile:
            values['mobile'] = mobile
        return values
