from odoo import models, fields, api


class ResPartner(models.Model):

    _inherit = "res.partner"


    instructor = fields.Boolean(string="Instructor", default=False)

    session_id = fields.Many2many("openacademy.session", string="Attended Sessions", readonly=True)