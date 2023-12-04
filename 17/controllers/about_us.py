from odoo import models, fields, api
import json                                  
from odoo import http                           
from odoo.http import request,Response          
import requests                                 
import ast
class AboutUs(http.Controller):
    @http.route('/AboutUs', auth="public",csrf=False, website=True, methods=['GET'])
    def get_aboutus(self): 
        result=[]
        headers = request.httprequest.headers
        try:
            aboutus_obj=request.env['about.us'].sudo().search([])
            check_list=lambda x:x[0] if x else {} 
            check_str=lambda x:x if x else ""
            for item in aboutus_obj:
                result.append({
                    'aboutUs':[{
                        'hero':check_list([{'image':check_str(hero.image_url),
                                            'title':check_str(hero.title)} for hero in aboutus_obj.hero_id]),
                        
                        'about':check_list([{  'title': check_str(about.title),
                                    'subTitle': check_str(about.subTitle),
                                    'text': check_str(about.text),
                                    'number': {
                                        'value': check_str(about.value),
                                        'description': check_str(about.description)} 
                                } for about in aboutus_obj]),
                        'values':check_list([{'item':[{'title':value.title,'text':value.text} for value in aboutus_obj.values_ids],'image':check_str(aboutus_obj.image_url)}]),  
                        
                        'brand':check_list([{'image':check_str(brand.image_url),
                                'description':{'title':check_str(brand.name),'text':check_str(brand.comment)}
                        } for brand in aboutus_obj.brand_id])
                    }]
                })
            if result:
                result=result[0]
            else:
                result={}    
            response = json.dumps({"data":result,'message' : 'about us'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])


