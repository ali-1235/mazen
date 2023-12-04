from odoo import models,api, fields,_
from odoo.exceptions import ValidationError
from datetime import datetime ,date,timedelta


class ContactUS(models.Model):
    _name = 'contact.us'
    _description = "this module is for contact.us "

    gender= fields.Selection([ 
        ('0','Mr.'),
        ('1','Mrs.'),
        ('2','Miss'),
    ], string='Gender')
    first_name = fields.Char(string='First Name', default='')
    last_name = fields.Char(string='Last Name', default='')
    company_name = fields.Char(string='Company Name', default='')
    designation = fields.Char(string='Designation ', default='')
    email = fields.Char(string='email', default='')
    area_code = fields.Char(string='Area Code', default='')
    phone = fields.Char(string='phone', default='')

    area_of_interest= fields.Selection([ 
        ('0','Hybrid IT'),
        ('1','Application & Business Intelligence'),
        ('2','Infrastructure'),
        ('3','Managed Services'),
        ('4','Others'),
    ], string='Area Of Interest')
    message = fields.Text(string='Message', default='')
    option_1 = fields.Boolean(string="I agree to SSTech’s Terms of use and acknowledge SSTech’s Privacy Policy.")
    option_2 = fields.Boolean(string="Opt in for Marketing Communication")
    country_id = fields.Many2one('res.country', string='Country')

