from odoo import models, fields, api
import json                                  
from odoo import http                           
from odoo.http import request,Response          
import requests                                 
import ast
class Home(http.Controller):
    @http.route('/Home', auth="public",csrf=False, website=True, methods=['GET'])
    def get_home(self): 
        result=[]
        headers = request.httprequest.headers

        try:
            home_obj=request.env['home'].sudo().search([])
            check_list = lambda x:x[0] if x else {}
            check_str = lambda x:x if x else ''
            for item in home_obj:
                result.append({
                    'home':check_list([{
                            'hero':[{
                                'title':check_str(hero.title),
                                'subTitle':check_str(hero.subTitle),
                                'image':check_str(hero.image_url)
                            } for hero in home_obj.hero_ids]
                        }])
                })
            if result:
                result=result[0]
            else:
                result={}    
            response = json.dumps({"data":result,'message' : 'home'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])  
