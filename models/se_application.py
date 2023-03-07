from odoo import fields,models

class SeApplication(models.Model):
    _name = 'se.application'
    _description = 'Se Application'


    first_name = fields.Char(
        'First Name', required=True, translate=True)
    middle_name = fields.Char(
        'Middle Name', translate=True)
    last_name = fields.Char(
        'Last Name', required=True)
    
    register_id = fields.Char(
        string='Register Id'
    )
    application_number = fields.Char(
        'Application Number')
        
    admission_date = fields.Date(
        'Admission Date')
    application_date = fields.Datetime(
        'Application Date',)
    course_id = fields.Char(
        'Course'
        )
    batch_id = fields.Char(
        'Course'
        )
    # batch_id = fields.Many2one(
    #     'op.batch', 'Batch', required=False,
    #     states={'done': [('readonly', True)],
    #             'submit': [('required', True)],
    #             'fees_paid': [('required', True)]})