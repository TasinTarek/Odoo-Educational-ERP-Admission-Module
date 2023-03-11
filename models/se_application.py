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

    ssc_gpa = fields.Float(string='SSC GPA')
    ssc_grade = fields.Char(string='SSC Grade')
    ssc_certificate = fields.Binary(string='SSC Academic Transcript',
                                    attachment=True, store=True, help="Applicant SSC Certificate.")
    is_golder_ssc = fields.Boolean(string='Is Golder in SSC?')
    # education_board_ssc_id = fields.Many2one(comodel_name='op.education.board', string='Education Board', domain=[
    #                                          ('academic_medium_type', '=', 'general')])
    
    education_board_ssc_id = fields.Selection(
        string='Education Board',
        selection=[('dhaka', 'Dhaka'), ('chattogram', 'Chattogram')]
    )
     
    roll_number_ssc = fields.Char(string='Roll No.')
    registration_number_ssc = fields.Char(string='Reg. No.')
    
    year_ssc = fields.Char(string='Year', stored=True)
    
    # admission_board_result_ssc_ids = fields.Many2one(
    #     'op.admission.board.result.general', string='Admission Board Results of SSC')
    # year_ssc = fields.Selection(lambda self: self._get_years(), string='Year', stored=True)
    hsc_gpa = fields.Float(string='HSC GPA')
    hsc_grade = fields.Char(string='HSC Grade')
    hsc_certificate = fields.Binary(string='HSC Academic Transcript',
                                     attachment=True, store=True, help="Applicant HSC Certificate.")
    is_golder_hsc = fields.Boolean(string='Is Golder in HSC?')
    # education_board_hsc_id = fields.Many2one(comodel_name='op.education.board', string='Education Board', domain=[
    #                                           ('academic_medium_type', '=', 'general')])
    education_board_hsc_id = fields.Selection(
        string='Education Board',
        selection=[('dhaka', 'Dhaka'), ('chattogram', 'Chattogram')]
    )
    roll_number_hsc = fields.Char(string='Roll No.')
    registration_number_hsc = fields.Char(string='Reg. No.')
    # # year_hsc = fields.Selection(lambda self: self._get_years(), string='Year', stored=True)
    year_hsc = fields.Char(string='Year', stored=True)
    # admission_board_result_hsc_ids = fields.One2many(
    #     'op.admission.board.result.general', 'admission_id', string='Admission Board Results of HSC', domain=[('exam_name_ref', '=', 'hsc')])
    # is_get_educational_board_result_ssc = fields.Boolean(
    #     string='Is Get Education Board Result of SSC?', default=False, readonly=True)
    # is_get_educational_board_result_hsc = fields.Boolean(
    #     string='Is Get Education Board Result of HSC?', default=False, readonly=True)

    # education_board_o_level_id = fields.Many2one(comodel_name='op.education.board', string='Exam Board', domain=[
    #                                              ('academic_medium_type', '=', 'english'), ('is_allow_for_o_level', '=', True)])
    # # passing_year_o_level = fields.Selection(lambda self: self._get_years(), string='Passing Year', stored=True)
    passing_year_o_level = fields.Char(string='Passing Year', stored=True)
    o_level_certificate = fields.Binary(
         string='O-Level Academic Transcript', attachment=True, store=True, help="Applicant O-Level Certificate.")
    education_board_o_level_id = fields.Selection(
        string='Education Board',
        selection=[('british', 'British'), ('american', 'American')]
    )
    # admission_board_result_o_level_ids = fields.One2many(
    #     'op.admission.board.result.english', 'admission_id', string='Admission Board Results of O-Level', domain=[('exam_name_ref', '=', 'o_level')])
    # education_board_a_level_id = fields.Many2one(comodel_name='op.education.board', string='Exam Board', domain=[
    #                                              ('academic_medium_type', '=', 'english'), ('is_allow_for_a_level', '=', True)])
    # # passing_year_a_level = fields.Selection(lambda self: self._get_years(), string='Passing Year', stored=True)
    passing_year_a_level = fields.Char(string='Passing Year', stored=True)
    a_level_certificate = fields.Binary(
         string='A-Level Academic Transcript', attachment=True, store=True, help="Applicant A-Level Certificate.")
    education_board_a_level_id = fields.Selection(
        string='Education Board',
        selection=[('british', 'British'), ('american', 'American')]
    )
    # admission_board_result_a_level_ids = fields.One2many(
    #     'op.admission.board.result.english', 'admission_id', string='Admission Board Results of A-Level', domain=[('exam_name_ref', '=', 'a_level')])
    # admission_board_result_all_certificate = fields.Binary(
    #     string='All Academic Certificate', attachment=True, store=True, help="Attach all the Academic Certificate in single document (PDF).")
    # admission_board_result_all_ids = fields.One2many(
    #     'op.admission.board.result.all', 'admission_id', string='Admission Board Results')

    # admission_achievement_ids = fields.One2many(
    #     'op.admission.achievement', 'admission_id', string='Admission Applicant Achievements')
    # admission_professional_experience_ids = fields.One2many(
    #     'op.admission.professional.experience', 'admission_id', string='Admission Applicant Professional Experiences')

# Personal Details
    signature = fields.Binary(string='Signature', attachment=True, store=True, help="Applicant signature.")
    passport = fields.Binary(string='Passport', attachment=True, store=True, help="Applicant passport.")
    gender = fields.Selection(
        [
            ('m', 'Male'),
            ('f', 'Female'),
            ('o', 'Other')
        ],
        string='Gender',
        required=False,
        states={'done': [('readonly', True)]}
    )
    birth_date = fields.Date('Birth Date', required=False, states={
                             'done': [('readonly', True)]})
    marital_status = fields.Selection(
        [
            ('single', 'Single'),
            ('married', 'Married'),
            ('divorced', 'Divorced'),
            ('widowed', 'Widowed'),
        ],
        string='Marital Status',
        store=True
    )
    email = fields.Char(string='Email')
    alternate_email = fields.Char(string='Alternate Email')
    emergency_contact_info = fields.Char(string='Emergency Contact')
    phone = fields.Char(String='Phone')
    mobile = fields.Char(String='Mobile')
    street = fields.Char()
    street2 = fields.Char()
    city = fields.Char()    
    state_id = fields.Char()
    zip = fields.Char()
    country_id = fields.Char()
     
    permanent_district_id = fields.Selection(
        string='Permanent District',
        selection=[('dhaka', 'Dhaka'), ('valor2', 'valor2')]
    )
    present_district_id = fields.Selection(
        string='Present District',
        selection=[('dhaka', 'Dhaka'), ('ctg', 'CTG')]
    )
    # will relation later with district model
    # permanent_district_id = fields.Many2one(
    #     comodel_name='op.district', string='Permanent District')
    is_permanent_present_address_same = fields.Boolean(
        string='Present Address same as Permanent Address')
    present_street = fields.Char()
    present_street2 = fields.Char()
    present_city = fields.Char()    
    present_state = fields.Char()
    present_zip = fields.Char()
    present_country_id = fields.Char()
    mailing_address = fields.Selection(
        [
            ('present_address', 'Present Address'),
            ('permanent_address', 'Permanent Address'),
            ('other_address', 'Other Address'),
        ],
        string='Mailing Address',
        store=True
    )
    is_permanent_present_address_same = fields.Boolean(
        string='Present Address same as Permanent Address')
    
    religion = fields.Selection(
        [
            ('islam', 'Islam'),
            ('hinduism', 'Hinduism'),
            ('christianity', 'Christianity'),
            ('buddhism', 'Buddhism'),
            ('other', 'Other'),
        ],
        string='Religion',
        store=True
    )
    blood_group = fields.Selection(
        [
            ('A+', 'A+ve'),
            ('B+', 'B+ve'),
            ('O+', 'O+ve'),
            ('AB+', 'AB+ve'),
            ('A-', 'A-ve'),
            ('B-', 'B-ve'),
            ('O-', 'O-ve'),
            ('AB-', 'AB-ve')
        ],
        string='Blood Group',
        store=True
    )
    whatsapp_number = fields.Char(string='WhatsApp No.')
    social_network = fields.Char(string='Social Network ID')
    birth_place = fields.Char(string='Place of Birth')
    national_country_id = fields.Char(
        string='Country')
    nationality = fields.Char(string='Nationality')
    passport_no = fields.Char(string='Passport No.')
    national_id_no = fields.Char(string='National ID No.')
    passport_expire_date = fields.Date(string='Passport Expire Date')
    visa_no = fields.Char(string='Visa No.')
    visa_expire_date = fields.Date(string='Visa Expire Date')
    
    know_the_diu_from_website = fields.Boolean(string='From, DIU Website')
    know_the_diu_from_newspaper = fields.Boolean(string='Newspaper')
    know_the_diu_from_social_media = fields.Boolean(string='Social Media')
    know_the_diu_from_sms = fields.Boolean(string='SMS')
    know_the_diu_from_daffodil_family = fields.Boolean(string='Daffodil Family')
    know_the_diu_from_diu_student = fields.Boolean(string='DIU Student')
    know_the_diu_from_diu_employee = fields.Boolean(string='DIU Employee')
    know_the_diu_from_others = fields.Boolean(string='Others')

    
    is_parents_freedom_fighter = fields.Boolean(
        string='If your parent is Freedom Fighter',
    )
    is_tribal = fields.Boolean(
        string='If you are a tribal',
    )
    is_physical_disorder = fields.Boolean(
        string='If you are physically disorder',
    )
    is_first_division_player = fields.Boolean(
        string='If you are a 1st division player',
    )
    
    # Parent Details

    father_name = fields.Char(string='Father Name')
    father_contact_number = fields.Char(string='Mobile')
    father_email = fields.Char(string='Email')
    father_national_id = fields.Char(string='National ID')
    father_passport = fields.Char(string='Passport')
    father_birthday = fields.Date(string='Date of Birth')
    father_age = fields.Float(string='Age')
    father_occupation = fields.Char(string='Occupation')
    father_company = fields.Char(string='Company Name')
    father_designation = fields.Char(string='Designation')
    father_annual_income = fields.Float(string='Annual Income', default=0)
    father_annual_income_currency_symbol = fields.Selection(
        [
            ('bdt', '৳'),
            ('dollar', '$'),
        ],
        string='Annual Income Currency Symbol',
        store=True
    )
    mother_name = fields.Char(string='Mother Name')
    mother_contact_number = fields.Char(string='Mobile')
    mother_email = fields.Char(string='Email')
    mother_national_id = fields.Char(string='National ID')
    mother_passport = fields.Char(string='Passport')
    mother_birthday = fields.Date(string='Date of Birth')
    mother_age = fields.Float(string='Age')
    mother_occupation = fields.Char(string='Occupation')
    mother_company = fields.Char(string='Company Name')
    mother_designation = fields.Char(string='Designation')
    mother_annual_income = fields.Float(string='Annual Income', default=0)
    mother_annual_income_currency_symbol = fields.Selection(
        [
            ('bdt', '৳'),
            ('dollar', '$'),
        ],
        string='Annual Income Currency Symbol',
        store=True
    )
        #local guardian
    local_guardian_name = fields.Char(string='Name')
    local_guardian_relation = fields.Char(string='Relationship')
    local_guardian_contact_number = fields.Char(string='Mobile')
    local_guardian_email = fields.Char(string='Email')
    local_guardian_national_id = fields.Char(string='National ID')
    local_guardian_passport = fields.Char(string='Passport')
    local_guardian_street = fields.Char(string='Street', size=256)
    local_guardian_street2 = fields.Char(string='Street2', size=256)
    local_guardian_city = fields.Char(string='City', size=64)
    local_guardian_state_id = fields.Char(string='States')
    local_guardian_zip = fields.Char(string='Zip', size=8)
    local_guardian_country_id = fields.Char(string='Country')

    expanse_bearer = fields.Selection(
        [
            ('father', 'Father'),
            ('mother', 'Mother'),
            ('other', 'Others'),
        ],
        string='Expense Bearer',
        store=True
    )
    expanse_bearer_name = fields.Char(string='Name')
    expanse_bearer_relation = fields.Char(string='Relationship')
    expanse_bearer_contact_number = fields.Char(string='Mobile')
    expanse_bearer_national_id = fields.Char(string='National ID')
    expanse_bearer_passport = fields.Char(string='Passport')
    expanse_bearer_birthday = fields.Date(string='Date of Birth')
    expanse_bearer_age = fields.Float(string='Age')
    expanse_bearer_employer_name = fields.Char(string='Employer Name')
    expanse_bearer_occupation = fields.Char(string='Occupation')
    expanse_bearer_company = fields.Char(string='Company Name')
    expanse_bearer_designation = fields.Char(string='Designation')
    expanse_bearer_annual_income = fields.Float(string='Annual Income', default=0)
    expanse_bearer_annual_income_currency_symbol = fields.Selection(
        [
            ('bdt', '৳'),
            ('dollar', '$'),
        ],
        string='Annual Income Currency Symbol',
        store=True
    )
    expanse_bearer_national_id_attachment = fields.Binary(string='Upload National ID', attachment=True, store=True, help="Upload Applicant Expanse Bearer National ID.")
    expanse_bearer_signature_attachment = fields.Binary(string='Upload Signature', attachment=True, store=True, help="Upload Applicant Expanse Bearer Signature.")
    expanse_bearer_street = fields.Char(string='Street', size=256)
    expanse_bearer_street2 = fields.Char(string='Street2', size=256)
    expanse_bearer_city = fields.Char(string='City', size=64)
    expanse_bearer_state_id = fields.Char(string='States')
    expanse_bearer_zip = fields.Char(string='Zip', size=8)
    expanse_bearer_country_id = fields.Char(string='Country')

    life_insurance = fields.Selection(
        [
            ('father', 'Father'),
            ('mother', 'Mother'),
            ('other', 'Others'),
        ],
        string='Life Insurance',
        store=True
    )
    life_insurance_name = fields.Char(string='Name')
    life_insurance_relation = fields.Char(string='Relationship')
    life_insurance_contact_number = fields.Char(string='Mobile')
    life_insurance_email = fields.Char(string='Email')
    life_insurance_national_id = fields.Char(string='National ID')
    life_insurance_passport = fields.Char(string='Passport')

    legal_guardian_name = fields.Char(string='Name')
    legal_guardian_date = fields.Date(string='Date', default = lambda self: fields.datetime.now())
    legal_guardian_signature_attachment = fields.Binary(string='Upload Signature', attachment=True, store=True, help="Upload legal guardian Signature.")
 
    other_street = fields.Char(string='Street')
    other_street2 = fields.Char(string='Street2')
    other_city = fields.Char(string='City')
    other_state_id = fields.Char(
         string='States')
    other_zip = fields.Char(string='Zip')
    
    # Manual Documents

    is_manual_photographs = fields.Boolean(string='Manual Photographs')
    is_manual_ssc_certificate = fields.Boolean(string='SSC/Equivalent')
    is_manual_hsc_certificate = fields.Boolean(string='HSC/Equivalent')
    is_manual_bachelor_certificate = fields.Boolean(string='Bachelor')
    is_manual_ssc_transcript = fields.Boolean(string='SSC/Equivalent')
    is_manual_hsc_transcript = fields.Boolean(string='HSC/Equivalent')
    is_manual_bachelor_transcript = fields.Boolean(string='Bachelor')
    is_manual_photocopies_student = fields.Boolean(string='Student')
    is_manual_photocopies_guardian = fields.Boolean(string='Guardian')
    is_manual_copies_other_relevant_certificate = fields.Boolean(string='Manual copies of other relevant Certificates')
    is_manual_bring_main_certificates_transcripts = fields.Boolean(string='Manual bring Main Certificates and Transcripts')
    
    # Payment Details
    # account_move_id = fields.Char(string="Invoice")
    # invoice_amount_total_string = fields.Char(string="Total Amount")
    # invoice_amount_residual_string = fields.Char(string="Amount Due")
    # invoice_amount_paid_string = fields.Char(string="Amount Paid")
    # invoice_payment_state = fields.Selection(string="Payment Status")
    # invoice_payment_mediums = fields.Date(string="Payment Date")

   
    # admission_fee_account_move_id = fields.Char(string="Invoice")
    # admission_fee_invoice_amount_total_string = fields.Char(string="Total Amount")
    # admission_fee_invoice_amount_residual_string = fields.Char(string="Amount Due")
    # admission_fee_invoice_amount_paid_string = fields.Char(string="Amount Paid")
    # admission_fee_invoice_payment_state = fields.Selection(string="Payment Status")
    # admission_fee_invoice_payment_state_allow_rel = fields.Selection(string="Payment Status (Based on Allow Amount)")
    # admission_fee_invoice_payment_mediums = fields.Text()
    # admission_fee_invoice_payment_date = fields.Date(string="Payment Date")
    