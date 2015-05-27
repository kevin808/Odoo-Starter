# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2015 Kevin Lee (<http://kevin808.lofter.com>)
#    Authors: Kevin Lee <likan2008@126.com>
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
import logging
from openerp import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)

class survey_page(models.Model):
    _inherit = 'survey.user_input'
    # seats = fields.Integer(string="Number of seats",required=False)
    # duration = fields.Float(digits=(6, 2), help="Duration in days")
    duration = fields.Float(string="The days you will get",compute='_duration')

    @api.multi
    # @api.depends('quizz_score','duration','survey_id')
    def _duration(self):
        # import pdb
        # pdb.set_trace()
        if len(self) > 1:
            if  self[0].quizz_score > self[1].quizz_score:
                self[0].duration = 0.0
                self[1].duration = 5.0
            elif self[0].quizz_score == self[1].quizz_score:
                if self[0].quizz_score == 0:
                    self[0].duration = 1.0
                    self[1].duration = 1.0
                else:
                    self[0].duration = 2.0
                    self[1].duration = 2.0                
            elif  self[0].quizz_score < self[1].quizz_score:
                self[0].duration = 5.0
                self[1].duration = 0.0
        else:
            pass
