# -*- coding: utf-8 -*-

import requests

from odoo import http, _
from odoo.http import request


def _finditem(obj, key):
    if key in obj:
        if isinstance(obj, dict):
            return obj[key]
    for k, v in obj.items():
        if isinstance(v, list):
            if isinstance(v[0], dict):
                item = _finditem(v[0], key)
                if item is not None:
                    return item


class DatarobotForm(http.Controller):

    @http.route(['/datarobot/form'], type='http', auth="public", website=True)
    def datarobot_form(self, **kwargs):
        if not request.session.uid:
            return http.redirect_with_hash('/web/login')
        return request.render("datarobot.datarobot_form", {})

    @http.route(['/datarobot/form/submit'], type='http', auth="public", website=True)
    def datarobot_form_submit(self, **kwargs):
        try:
            spreadsheet_url = kwargs.get('spreadsheet_url')
            if 'docs.google.com/spreadsheets' in spreadsheet_url:
                api_key = request.env['ir.config_parameter'].sudo().get_param('google_sheet_api_key')
                splitted_url = spreadsheet_url.split("/")
                spreadsheet_id = splitted_url[splitted_url.index('d')+1]
                request_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}?key={api_key}"
                spreadsheet_data = requests.get(request_url).json()
                if spreadsheet_data.get('error'):
                    return request.render('http_routing.http_error', {
                        'status_code': _('Oops! Status code: {}'.format(spreadsheet_data['error']['code'])),
                        'status_message': _("""{}.""".format(spreadsheet_data['error']['message']))})
                sheets = None
                if spreadsheet_data.get('sheets'):
                    sheets = [i['properties']['title'] for i in spreadsheet_data['sheets']]
                sheet_types = []
                if sheets:
                    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                    for sheet in sheets:
                        for char in alphabet:
                            sheet_range = f"{char}1:{char}1"
                            sheet_request_url = 'https://sheets.googleapis.com/v4/spreadsheets/{}'\
                                                '?ranges={}!{}&fields=sheets(data(rowData(values'\
                                                '(userEnteredFormat%2FnumberFormat%2CuserEnteredValue))'\
                                                '%2CstartColumn%2CstartRow))&key={}'.format(
                                                spreadsheet_id, sheet, sheet_range, api_key)
                            sheet_data = requests.get(sheet_request_url).json()
                            if sheet_data.get('error'):
                                break
                            if not sheet_data['sheets'][0]['data'][0]:
                                break
                            if not sheet_data['sheets'][0]['data'][0].get('rowData'):
                                continue
                            else:
                                try:
                                    value = _finditem(sheet_data['sheets'][0]['data'][0], 'userEnteredValue')
                                    guess_type = list(value.keys())[0]
                                    if guess_type == 'stringValue':
                                        sheet_types.append('string') 
                                    elif guess_type == 'numberValue':
                                        values_data = sheet_data['sheets'][0]['data']\
                                                        [0].get('rowData')[0]['values'][0]
                                        if values_data.get('userEnteredFormat'):
                                            number_format = values_data.get('userEnteredFormat')['numberFormat']['type']
                                            if number_format == 'DATE':
                                                sheet_types.append('date')
                                        else:
                                            sheet_types.append('number')
                                    elif guess_type == 'boolValue':
                                        sheet_types.append('boolean')
                                except Exception:
                                    pass
                else:
                    return request.render('http_routing.http_error', {
                        'status_code': _('Oops'),
                        'status_message': _("""The requested Google Spreadsheet Link doesn't contain any sheet.""")})
                sheet_types = set(sheet_types)
                return request.render("datarobot.user_form_success", {'sheet_types': sheet_types})
            else:
                return request.render("datarobot.user_form_warning", {})
        except Exception:
            return request.render('http_routing.http_error', {
                'status_code': _('Oops'),
                'status_message': _("""The requested page is invalid, or doesn't exist anymore.""")})
