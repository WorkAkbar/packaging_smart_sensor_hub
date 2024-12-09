from odoo import models, fields

class QualityCheck(models.Model):
    _name = 'quality.check'
    _description = 'Quality Check'

    batch_number = fields.Char(string='Batch Number', required=True)
    defects = fields.Integer(string='Defects Count')
    defect_type = fields.Text(string='Defect Type')
    status = fields.Selection([
        ('passed', 'Passed'),
        ('failed', 'Failed'),
    ], string='Status', default='passed')
