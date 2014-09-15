from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from lxml import etree as ET



class project_logical_framework_project(osv.Model):
    _inherit = 'project.project'

    _columns = {
        'go': fields.text('Global objectives'),
        'go_it': fields.text('Global objectives - Interventions'),
        'go_in': fields.text('Global objectives - Indicators'),
        'go_src': fields.text('Global objectives - Verification source'),
        'go_hy': fields.text('Global objectives - Hypothesis'),

        'so': fields.text('Specefic objectives - '),
        'so_it': fields.text('Specefic objectives - Interventions'),
        'so_in': fields.text('Specefic objectives - Indicators'),
        'so_src': fields.text('Specefic objectives - Verification source'),
        'so_hy': fields.text('Specefic objectives - Hypothesis'),

        'res': fields.text('Results - '),
        'res_it': fields.text('Results - Interventions'),
        'res_in': fields.text('Results - Indicators'),
        'res_src': fields.text('Results - Verification source'),
        'res_hy': fields.text('Results - Hypothesis'),

        'act': fields.text('Activities - '),
        'act_it': fields.text('Activities - Interventions'),
        'act_in': fields.text('Activities - Indicators'),
        'act_src': fields.text('Activities - Verification source'),
        'act_hy': fields.text('Activities - Hypothesis'),
    }