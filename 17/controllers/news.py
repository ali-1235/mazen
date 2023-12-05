from odoo import models, fields, api
import json                                  
from odoo import http                           
from odoo.http import request,Response          
import requests                                 
import ast
class News(http.Controller):
    @http.route('/News', auth="public",csrf=False, website=True, methods=['GET'])
    def get_all_news(self): 
        result=[]
        headers = request.httprequest.headers
        try:
            news_obj=request.env['news'].sudo().search([])
            check_list=lambda x:x[0] if x else {} 
            check_str=lambda x:x if x else ""
            for item in news_obj:
                result.append({
                    'image': check_str(item.image_url),
                    'title': check_str(item.title),
                    'content':check_str(item.content),
                    'slug': check_str(item.slug),
                    'tag': check_str(item.tag)
                })
             
            response = json.dumps({"news":result,'message' : 'All News'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])

    @http.route('/NewsBySlug/<string:slug>', auth="public",csrf=False, website=True, methods=['GET'])
    def get_NewsBySlug(self,slug): 
        result=[]
        headers = request.httprequest.headers
        try:
            news_obj=request.env['news'].sudo().search([('slug','=',slug)])
            check_list=lambda x:x[0] if x else {} 
            check_str=lambda x:x if x else ""
            for item in news_obj:
                result.append({
                    'image': [check_str(image.image_url) for image in item.news_detailed_ids],
                    'title': check_str(item.title),
                    'content':check_str(item.content),
                })
            if result:
                result=result[0]
            else:
                result={}    
            response = json.dumps({"newsDetailed":result,'message' : 'News Details'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])            