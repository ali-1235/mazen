from odoo import models,api, fields,_
from odoo.exceptions import ValidationError
from datetime import datetime ,date,timedelta


class Hero17(models.Model):
    _name = 'hero'
    _description = "this module is for Hero 17"


    image = fields.Image(string='image')
    image_url= fields.Char(string='image url',compute='_compute_image_url')
    title= fields.Char(string='title',default='')
    subTitle = fields.Char(string='subTitle', default='')

    @api.depends('image')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for obj in self:
            if obj.image:
                obj.image_url= base_url + '/web/image?' + 'model=hero&id=' + str(obj.id) + '&field=image'
            else :
                obj.image_url= ''


class values17(models.Model):
    _name = 'values'
    _description = "this module is for values 17"

    
    title = fields.Char(string='title',default=' ')
    text =  fields.Html(string='text',default='')




class Partner17(models.Model):
    _inherit = 'res.partner'

    image_url= fields.Char(string='image url',compute='_compute_image_url')
    category_ids = fields.Many2many('category' , string='category_ids')

    @api.depends('image_1920')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for obj in self:
            if obj.image_1920:
                obj.image_url= base_url + '/web/image?' + 'model=res.partner&id=' + str(obj.id) + '&field=image_1920'
            else :
                obj.image_url= ''


class AboutUS17(models.Model):
    _name = 'about.us'
    _description = "this module is for about us 17"

    hero_id = fields.Many2one('hero', string='hero')
    brand_id = fields.Many2one('res.partner', string='brand')
    values_ids = fields.Many2many('values' , string='values')
    image = fields.Image(string='values image')
    image_url= fields.Char(string='image url',compute='_compute_image_url')
    title = fields.Char(string='title', default=' ')
    subTitle = fields.Char(string='subTitle', default=' ')
    text =  fields.Html(string='text',default='')
    value = fields.Char(string='value', default=' ')
    description = fields.Html(string='description',default='')

    @api.depends('image')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for obj in self:
            if obj.image:
                obj.image_url= base_url + '/web/image?' + 'model=hero&id=' + str(obj.id) + '&field=image'
            else :
                obj.image_url= ''