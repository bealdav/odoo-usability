# -*- encoding: utf-8 -*-
##############################################################################
#
#    Base Fix Display Address module for OpenERP
#    Copyright (C) 2014 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
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

from openerp.osv import orm


class res_partner(orm.Model):
    _inherit = 'res.partner'

    def _display_address(
            self, cr, uid, address, without_company=False, context=None):
        '''Remove empty lines'''
        res = super(res_partner, self)._display_address(
            cr, uid, address, without_company=without_company, context=context)
        while "\n\n" in res:
            res = res.replace('\n\n', '\n')
        return res
