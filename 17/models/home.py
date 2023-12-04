from odoo import models,api, fields,_
from odoo.exceptions import ValidationError
from datetime import datetime ,date,timedelta


class Home17(models.Model):
    _name = 'home'
    _description = "this module is for Home "

    hero_ids = fields.Many2many('hero' , string='heros')

