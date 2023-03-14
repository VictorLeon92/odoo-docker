# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class CommercialController(http.Controller):

    @http.route('/api/commercials', auth='public', method=['GET'], csrf=False)
    def get_commercials(self, **kw):
        try:
            visits = http.request.env['versys.commercial'].sudo().search_read([], ['id', 'commercial_name', 'client_name', 'client_id'])
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

