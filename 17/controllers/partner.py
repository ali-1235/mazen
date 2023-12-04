from odoo import models, fields, api
import json                                  
from odoo import http                           
from odoo.http import request,Response          
import requests                                 
import ast
class Partner(http.Controller):
    @http.route('/Partners', auth="public",csrf=False, website=True, methods=['GET'])
    def get_aboutus(self): 
        result=[]
        headers = request.httprequest.headers
        try:
            hero_obj=request.env['hero'].sudo().search([],limit=1)
            partner_obj=request.env['res.partner'].sudo().search([])
            print(hero_obj)
            check_list=lambda x:x[0] if x else {} 
            check_str=lambda x:x if x else ""
            get_cat=lambda x:x.display_name if x else ''
            for item in hero_obj:
                result.append({
                    # 'partners':check_list([{
                        'hero':{'image':check_str(item.image_url),'title':check_str(item.title),'subTitle':check_str(item.subTitle)},
                    'partnerList':[{'image':partner.image_url,'category':get_cat(check_list([cat for cat in partner.category_id]))} for partner in partner_obj]
                    # }
                    # ])
                })
                
            if result:
                result=result[0]
            else:
                result={}    
            response = json.dumps({"partners":result,'message' : 'Partner'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])