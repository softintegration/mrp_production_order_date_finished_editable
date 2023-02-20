# -*- coding: utf-8 -*- 

import datetime

from odoo import models, fields, api, _


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def button_mark_done(self):
        date_finished_by_production = {}
        # we have to keep the date finished specified manually by the user to prevent losing them (will be overwritten by the super method)
        for production in self:
            date_finished_by_production.update({production.id:production.date_finished})
        res = super(MrpProduction,self).button_mark_done()
        for production in self:
            production._update_date_finished(date_finished_by_production[production.id])
        return res

    def _update_date_finished(self,new_date_finished):
        self.ensure_one()
        if not new_date_finished:
            return
        self.write({'date_finished':new_date_finished})
        self.workorder_ids.write({'date_finished':new_date_finished})
        self.move_finished_ids.write({'date':new_date_finished})
        self.move_finished_ids.mapped("move_line_ids").write({'date':new_date_finished})
        self.move_raw_ids.write({'date':new_date_finished})
        self.move_raw_ids.mapped("move_line_ids").write({'date':new_date_finished})
        return
