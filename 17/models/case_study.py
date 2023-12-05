from odoo import models,api, fields,_
from odoo.exceptions import ValidationError
from datetime import datetime ,date,timedelta


class CaseStudy(models.Model):
    _name = 'case.study'
    _description = "this module is for case study "

    
    
    title = fields.Char(string='Title', default='')
    description = fields.Char(string='Description', default='')
    slug = fields.Char(string='Slug', default='')
    industyr = fields.Text(string='Industyr', default='')
    aboutTheCompany =  fields.Html(string='AboutTheCompany',default='')

    
    businessChallanges_items = fields.One2many('business.item', 'business_id', string='Business Challanges')
    solution_items = fields.One2many('solution.item', 'solution_id', string='Solution')
    outcome_items = fields.One2many('outcome.item', 'outcome_id', string='Outcome')

class BusinessItem(models.Model):
    _name = 'business.item'

    name = fields.Char(string='Item Name')
    business_id = fields.Many2one('case.study', string='List')

class SolutionItem(models.Model):
    _name = 'solution.item'

    name = fields.Char(string='Item Name')
    solution_id = fields.Many2one('case.study', string='List')

class SolutionItem(models.Model):
    _name = 'outcome.item'

    name = fields.Char(string='Item Name')
    outcome_id = fields.Many2one('case.study', string='List')    

'''
    "solution": "ul (list)",
    "outcome": "ul (list)"
    '''
    
    # tag = fields.Char(string='tag', default='')
    


