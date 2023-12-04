from odoo import models,api, fields,_
from odoo.exceptions import ValidationError
from datetime import datetime ,date,timedelta


class LeaderShip17(models.Model):
    _name = 'leader.ship'
    _description = "this module is for LeaderShip 17 "

    hero_id = fields.Many2one('hero', string='hero')
    leadership_ids = fields.One2many('leader.sheip.line' , 'leader_id' , string='Leader Ship IDs')

class LeaderShipLines(models.Model):
    _name = 'leader.sheip.line'
    _description = "this module is for leader sheip line"

    leader_id = fields.Many2one('leader.ship')
    image = fields.Image(string='image')
    image_url = fields.Char(string='image url',compute='_compute_image_url')
    name = fields.Char(string='name',default='')
    title = fields.Char(string='title',default='')
    description = fields.Char(string='description',default='')



    @api.depends('image')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for obj in self:
            if obj.image:
                obj.image_url= base_url + '/web/image?' + 'model=leader.ship&id=' + str(obj.id) + '&field=image'
            else :
                obj.image_url= ''

    
