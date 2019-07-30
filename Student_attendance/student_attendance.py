# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, tools, api, models
from openerp.exceptions import ValidationError


class student_attendance(models.Model):
    _name = 'student.attendance'

    @api.multi
    def _get_image(self, name, args):
        return dict((p.id, tools.image_get_resized_images(p.image)) for p in self)
    @api.one
    def _set_image(self, name, value, args):
        return self.write({'image': tools.image_resize_image_big(value)})


    name = fields.Char('Student Name')
    month = fields.Selection([
                ('january', 'January'),
                ('february', 'February'),
                ('march', 'March'),
                ('april', 'April'),
                ('may', 'May'),
                ('june', 'June'),
                ('july', 'July'),
                ('august', 'August'),
                ('september', 'September'),
                ('october', 'October'),
                ('november', 'November'),
                ('december', 'December')], 'Month', required=True)
    total = fields.Integer('Total Attendance')
    presence = fields.Integer('Present Days')
    grade1 = fields.Float('Grade 1')
    grade2 = fields.Float('Grade 2')
    average = fields.Float(compute='avg', store='True')
    teacher_ids = fields.Many2many('teacher.attendance',
                                   string="Teacher")
    #image attache
    image = fields.Binary("Image",
                           help="This field holds the image used as avatar for this contact, limited to 1024x1024px")




    @api.depends('grade1', 'grade2')
    def avg(self):
        for record in self:
            record.average = (record.grade1 + record.grade2)/2


    #Constrains (Condition - message error)
    @api.constrains('grade1')
    def _check_something(self):
        for record in self:
            if record.grade1 > 20:
                raise ValidationError("Your grade is invalide: %s" % record.grade1)


    def print_quotation(self, cr, uid, ids, context=None):
        '''
        This function prints the sales order and mark it as sent, so that we can see more easily the next step of the workflow
        '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        self.signal_workflow(cr, uid, ids, 'quotation_sent')
        return self.pool['report'].get_action(cr, uid, ids, 'Student_attendance.report_studentattendancelist', context=context)









