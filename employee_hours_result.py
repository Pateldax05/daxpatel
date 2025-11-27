
from odoo import models, fields

class EmployeeHoursResult(models.TransientModel):
    _name = "employee.hours.result"
    _description = "Display result days"

    result_html = fields.Html(readonly=True)
