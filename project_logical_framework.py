from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from lxml import etree as ET

class project_logical_framework_project(osv.Model):
    _inherit = 'project.project'

    _columns = {
        'logical_framework' : fields.one2many(
            'project_logical_framework.logical_framework',
            'project_id',
            'Logical Framework'),
    }


class project_logical_framework_logical_framework(osv.Model):
    _name = 'project_logical_framework.logical_framework'

    _order = "type"

    def _logiquetitle(self, cr, uid, ids, field_name, arg, context):
        res = {}

        record = self.browse(cr, uid, ids, context=context)
        for data in record:
            res_str = dict(self.pool.get('project_logical_framework.logical_framework').fields_get(cr, uid, allfields=['type'], context=context)['type']['selection'])[data.type]
            res_str += "\n" + data.logique
            res[data.id] = res_str
        return res


    _columns = {
        'project_id' : fields.many2one(
            'project.project',
            'logical_framework',
            'Project'),

        'type': fields.selection((
            ('1','Global Objectives:'),
            ('2','Specific Objectives:'),
            ('3','Results:'),
            ('4','Activities:')),
                   'Type', required="true"),
        'logique': fields.text('Logique'),
        'logiquetitle': fields.function(_logiquetitle, type="text"),
        'intervention': fields.text('Intervention'),
        'indicators': fields.text('Indicators'),
        'verification': fields.text('Verification source'),
        'hypothesis': fields.text('Hypothesis'),
    }