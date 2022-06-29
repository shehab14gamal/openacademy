from odoo import models, fields, api


class Course(models.Model):

    _name = "openacademy.course"
    _description="Courses"

    name = fields.Char(string="Course Name", required =True)
    description = fields.Text(string="Description", help="add some description")
    responsible_id = fields.Many2one("res.users", string="responsible")

class Session(models.Model):
    _name = "openacademy.session"
    _description = "openacademy session"


    name = fields.Char(requered=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="duration in days")
    seats = fields.Integer(string="number of seats")
    instructor = fields.Many2one("res.partner", string="instructor")
    country_id = fields.Many2one(related='instructor.country_id')
    course = fields.Many2one("openacademy.course", string="course")
    attendee_id = fields.Many2many("res.partner" , string="Attendees", domain=[('city','=','Fremont')])



