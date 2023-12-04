from odoo import models, fields, api
import json                                  
from odoo import http                           
from odoo.http import request,Response          
import requests                                 
import ast
class ContactUS(http.Controller):
    
    @http.route('/Countries', auth="public",csrf=False, website=True, methods=['GET'])
    def get_all_country(self): 
        result=[]
        headers = request.httprequest.headers

        try:
            country_obj=request.env['res.country'].sudo().search([])
            for item in country_obj:
                result.append({
                    'id':item.id,
                    'name':item.name
                })
            response = json.dumps({"Countries":result,'message' : 'All Countries'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])  
    @http.route('/ContactUS', auth="public",csrf=False, website=True, methods=['POST'])
    def post_contact_us(self,**kw): 
        result=[]
        headers = request.httprequest.headers

        try:
            contatc_obj=request.env['contact.us'].sudo().create(kw)
            response = json.dumps({"data":[],'message' : 'Done'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])  
