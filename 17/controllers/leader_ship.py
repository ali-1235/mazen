from odoo import models, fields, api
import json                                  
from odoo import http                           
from odoo.http import request,Response          
import requests                                 
import ast
class LeaderShip(http.Controller):
    @http.route('/LeaderShip', auth="public",csrf=False, website=True, methods=['GET'])
    def get_leaderShip(self): 
        result=[]
        headers = request.httprequest.headers

        try:
            leader_ship_obj=request.env['leader.ship'].sudo().search([])
            check_list=lambda x:x[0] if x else {}
            check_str=lambda x:x if x else ''
            for item in leader_ship_obj:
                result.append({
                    'leaderShip':check_list([{'hero':check_list([{ 'image':check_str(hero.image_url),
                                                                    'title':check_str(hero.title)
                                                                    } for hero in leader.hero_id]),
                                            'leaderShipList':[{'image':check_str(line.image_url),
                                                                'name':check_str(line.title),
                                                                'title':check_str(line.title),
                                                                'description':check_str(line.description)
                                                                } for line in leader.leadership_ids]} 
                                            for leader in leader_ship_obj])
                            })
            if result:
                result=result[0]
            else:
                result={}    
            response = json.dumps({"data":result,'message' : 'leaderShip'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)]) 