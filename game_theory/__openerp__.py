# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2015 Kevin Lee (<http://kevin808.lofter.com>)
#    Kevin Lee <likan2008@126.com>
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
{
    'name': 'Game theory',
    'version': '1.0',
    'category': '',
    'summary': '',
    'description': """
Game theory.
====================================

New gorup: Play Games
--------------------------------------------
    * manage own products
    * modify own profile data
    """,
    'author': 'Kevin Lee',
    'website': 'http://kevin808.lofter.com',
    'images': [],
    'depends': [
        'survey',
    ],
    'data': [
        'theory_view.xml',
    ],
    'installable': True,
}