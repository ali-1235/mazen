from odoo import models, fields, api
import json                                  
from odoo import http                           
from odoo.http import request,Response          
import requests                                 
import ast
class CaseStudy(http.Controller):
    @http.route('/CaseStudy', auth="public",csrf=False, website=True, methods=['GET'])
    def get_all_caseStudy(self): 
        result=[]
        headers = request.httprequest.headers
        try:  
            case_obj=request.env['case.study'].sudo().search([])
            check_list=lambda x:x[0] if x else {} 
            check_str=lambda x:x if x else ""
            for item in case_obj:
                result.append({
                    'title': check_str(item.title),
                    'description': check_str(item.description),
                    'slug': check_str(item.slug)
                })

            response = json.dumps({"caseStudy":result,'message' : 'All Case Study'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])

    @http.route('/CaseStudyBySlug/<string:slug>', auth="public",csrf=False, website=True, methods=['GET'])
    def get_CaseStudyBySlug(self,slug): 
        result=[]
        headers = request.httprequest.headers
        try:
            case_obj=request.env['case.study'].sudo().search([('slug','=',slug)])
            check_list=lambda x:x[0] if x else {} 
            check_str=lambda x:x if x else ""
            for item in case_obj:
                result.append({
                    'industyr': check_str(item.industyr),
                    'aboutTheCompany':check_str(item.aboutTheCompany),
                    'businessChallanges': [check_str(business.name) for business in item.businessChallanges_items],
                    'solution': [check_str(solution.name) for solution in item.solution_items],
                    'outcome': [check_str(outcome.name) for outcome in item.outcome_items]
                })
            if result:
                result=result[0]
            else:
                result={}    
            response = json.dumps({"caseStudyByToken":result,'message' : 'Case Study Details'}) 
            return Response(
                response, status=200,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])    

        except Exception as e:
            response = json.dumps({'data':{},'message':str(e)}) 
            return Response(
                response, status=500,
                headers=[('Content-Type', 'application/json'), ('Content-Length', 100)])            