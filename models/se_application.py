from odoo import fields,models,api

class SeApplication(models.Model):
    _name = 'se.application'
    _inherit = ('se.venue','mail.thread')
    _description = 'Se Application'


    first_name = fields.Char(
        'First Name', required=True, translate=True)
    middle_name = fields.Char(
        'Middle Name', translate=True)
    last_name = fields.Char(
        'Last Name', required=True)
    
    applicant_photo = fields.Image(string='Photo', attachment=True, store=True)
      
    is_alumni = fields.Boolean(
        string='Is Alumni ?',
    )
    student_id = fields.Char(
        string='Student ID'
    )
    # register_id = fields.Char(
    #     string='Register Id'
    # )
    
    register_id = fields.Many2one(
        string='Register ID',
        comodel_name='se.admission',
        
    )
    
    application_number = fields.Char(
        'Application Number')
    admission_date = fields.Date(
        'Admission Date')
    admission_expire_date = fields.Date(
        'Admission Expire Date')
    application_date = fields.Datetime(
        'Application Date',)
    course_id = fields.Char(
        'Course'
        )
    batch_id = fields.Char(
        'Course'
        )
    curriculum_id = fields.Char(
        'Curriculum '
        )
    order_id = fields.Char(
        'Registration Fees Ref'
    )
    batch_id = fields.Char('Batch')

    #     'op.batch', 'Batch', required=False,
    #     states={'done': [('readonly', True)],
    #             'submit': [('required', True)],
    #             'fees_paid': [('required', True)]})
    application_serial_number = fields.Char('Application Serial Number')
    fees = fields.Float('Admission Form Fee')
    admission_fee = fields.Float('Admission Fee')
    fees_term_id = fields.Char('Fees Term')
    academic_faculty_id = fields.Char('Academic Faculty')
    department_id = fields.Char('Department')
    semester_year_string = fields.Date('Year')
    semester_id = fields.Char('Semester')
    semester_type = fields.Char('Semester Type')
    # Academic

    
    form_type = fields.Selection(
        string='Apply Type',
        selection=[('local_bachelor_program_hsc', 'Local-Bachelor Program - HSC'),
                   ('local_bachelor_program_a_level', 'Local-Bachelor Program - A-Level'),
                   ('local_bachelor_program_diploma',
                    'Local-Bachelor Program - Diploma'),
                   ('local_masters_program_bachelor',
                    'Local-Masters Program - Bachelor'),
                   ('international_bachelor_program_a_level',
                    'International-Bachelor Program '),
                    ('international_masters_program', 'International - Masters Program'),
                   
                   ]
    )
    
    student_type_id = fields.Selection(
        string='Student Type',
        selection=[('local', 'Local'), ('international', 'International')]
    )
    education_shift_id = fields.Char('Education Shift')
     
    campus_id = fields.Many2one(
        string='Campus',
        comodel_name='se.venue',
        ondelete='restrict',
    )
    form_apply_type = fields.Selection(
        [
            ('direct', 'Direct'),
            ('online', 'Online'),
        ],
        string='Form Apply Type',
        default='direct',
        store=True
    )
    admission_type = fields.Selection(
        [
            ('direct', 'Direct Admission'),
            ('online', 'Online Admission'),
        ],
        string='Admission Type',
        store=True
    )
    academic_medium_type = fields.Selection(
        [
            ('general', 'General'),
            ('english', 'English'),
        ],
        string='Academic Medium',
        store=True
    )
    campus_type = fields.Selection(
        [
            ('on_campus', 'On Campus'),
            ('off_campus', 'Off Campus'),
        ],
        string='Campus Type',
        default='on_campus',
        store=True
    )
    
    eligibility_state = fields.Selection(
        string='Eligibility Status',
        selection=[('uncheck', 'Not Verified'),
                   ('approve', 'Verified'), ('reject', 'Rejected')]
    )
    eligibility_applicant_state = fields.Selection(
        string='Applicant Status',
        selection=[('uncheck', 'Uncheck'),
                   ('agree', 'Agree'), ('disagree', 'Disagree')]
    )
    is_eligible_for_admission_test = fields.Boolean(
        string='Is Eligible Admission for Test?', default=False)
    
    admission_test_date = fields.Datetime(string='Admission Test Date')
    admission_test_venue_id = fields.Many2one(
        comodel_name='se.venue', string='Admission Test Venue')
    result_publish_date = fields.Datetime(string='Result Publish Date')

     
    submit_form = fields.Char(
        string='Submit',
    )
    confirm_cancel = fields.Char(
        string='Cancel',
    )

    #Function

