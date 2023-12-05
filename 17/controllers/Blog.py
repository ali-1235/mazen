from odoo import models, fields, api
import json                                  
from odoo import http                           
from odoo.http import request,Response          
import requests                                 
import ast
class BlogNews(http.Controller):
    @http.route('/Blog', auth="public",csrf=False, website=True, methods=['GET'])
    def get_all_blog(self): 
        result=[]
        headers = request.httprequest.headers
        try:
            blog_obj=request.env['blog'].sudo().search([])
            check_list=lambda x:x[0] if x else {} 
            check_str=lambda x:x if x else ""
            for item in blog_obj:
                result.append({
                    'image': check_str(item.image_url),
                    'title': check_str(item.title),
                    'content':check_str(item.content),
                    'slug': check_str(item.slug),
                    'tag': check_str(item.tag)
                })
             
            response = json.dumps({"blog":result,'message' : 'All Blogs'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])

    @http.route('/blogBySlug/<string:slug>', auth="public",csrf=False, website=True, methods=['GET'])
    def get_blogBySlug(self,slug): 
        result=[]
        headers = request.httprequest.headers
        try:
            blog_obj=request.env['blog'].sudo().search([('slug','=',slug)])
            check_list=lambda x:x[0] if x else {} 
            check_str=lambda x:x if x else ""
            for item in blog_obj:
                result.append({
                    'image': check_str(item.image_url),
                    'title': check_str(item.title),
                    'content':check_str(item.content),
                })
            if result:
                result=result[0]
            else:
                result={}    
            response = json.dumps({"blogDetails":result,'message' : 'Blog Details'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])            