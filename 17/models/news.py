from odoo import models,api, fields,_
from odoo.exceptions import ValidationError
from datetime import datetime ,date,timedelta


class News(models.Model):
    _name = 'news'
    _description = "this module is for news "


    image = fields.Image(string='Image')
    image_url= fields.Char(string='Image url',compute='_compute_image_url')
    title = fields.Char(string='Title', default='')
    content =  fields.Html(string='Content',default='')
    slug = fields.Char(string='Slug', default='')
    tag = fields.Char(string='tag', default='')
    news_detailed_ids = fields.One2many('news.line.detailed' , 'news_id' , string='News Detailed')
    @api.depends('image')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for obj in self:
            if obj.image:
                obj.image_url= base_url + '/web/image?' + 'model=news&id=' + str(obj.id) + '&field=image'
            else :
                obj.image_url= ''

class NewsDetailed(models.Model):
    _name = 'news.line.detailed'
    _description = "this module is for news line detailed"

    news_id = fields.Many2one('news')
    # title = fields.Char(string='Title', default='')
    # content =  fields.Html(string='Content',default='')
    image = fields.Image(string='Image')
    image_url= fields.Char(string='Image url',compute='_compute_image_url')

    @api.depends('image')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for obj in self:
            if obj.image:
                obj.image_url= base_url + '/web/image?' + 'model=news.line.detailed&id=' + str(obj.id) + '&field=image'
            else :
                obj.image_url= ''