# -*- coding: utf-8 -*-

from odoo import models, fields, api


class se_admission(models.Model):
     _name = 'se.admission'
     _description = 'Admission'

     name = fields.Char(
        string='Name',
    )
     course = fields.Char(
        string='Course',
    )
     batch = fields.Char(
        string='Batch',
    )
     admission_form_fee = fields.Integer(
        string='Admission Form Fee',
    )
    
     fees_term = fields.Integer(
        string='Fees Term',
    )
    
     intake_no = fields.Integer(
        string='Intake No:',
    )
    
     minimum_admission = fields.Integer(
         string='Minimum Number. of Admission',
    )
     maximum_admission = fields.Integer(
        string='Maximum Number. of Admission',
    )   
     start_date = fields.Date(
        string='Start Date',
        default=fields.Date.context_today,
    )
    
     end_date = fields.Date(
        string='End Date',
        default=fields.Date.context_today,
    )
    
     admission_test_date = fields.Datetime(
        string='Admission Test Date',
        default=fields.Datetime.now,
    )
     
     result_publish_date = fields.Datetime(
         string='Result Publish Date',
         default=fields.Datetime.now,
     )
     
      
     venue_ids = fields.Many2many('se.venue', string='Venues')

     admission_fee_id = fields.Char(
         string='Admission Fee',
     )
     
     amount_admission_fee = fields.Integer(
         string='Admission Fee Amount',
     )
     academic_faculty_id = fields.Char(
          string = 'Academic Faculty'
     )
     department_id = fields.Char(
          string = 'Department'
     )
     semester_id = fields.Char(
          string = 'Semester'
     )
     semester_year = fields.Date(
          string='Year', track_visibility='onchange'
     )
     semester_type = fields.Char(
          string = 'Semester Type'
     )
     is_local_bachelor_program_hsc = fields.Boolean(
          string='Local - Bachelor Program - HSC', default=False
     )
     is_local_bachelor_program_a_level = fields.Boolean(
          string='Local - Bachelor Program - A-Level', default=False
     )
     is_local_bachelor_program_diploma = fields.Boolean(
          string='Local - Bachelor Program - Diploma', default=False
     )
     is_local_masters_program_bachelor = fields.Boolean(
          string='Local - Masters Program - Bachelor', default=False
     )
     is_international_bachelor_program = fields.Boolean(
          string='International - Bachelor Program', default=False
     )
     is_international_masters_program = fields.Boolean(
          string='International - Masters Program', default=False
     )
     
     campus_id = fields.Text(string="Daffodil Smart City")
     admission_eligibility = fields.Text(string='Eligibility') 