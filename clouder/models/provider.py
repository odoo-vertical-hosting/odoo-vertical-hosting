# -*- coding: utf-8 -*-
# Copyright 2015 Clouder SASU
# License LGPL-3.0 or later (http://gnu.org/licenses/lgpl.html).

import logging

from openerp import api
from openerp import fields
from openerp import models


_logger = logging.getLogger(__name__)


class ClouderProvider(models.Model):

    _name = 'clouder.provider'
    _description = 'Provider'

    name = fields.Char('Name')
    config_id = fields.Many2one('clouder.config.settings',
                                'Configuration', required=True)
    type = fields.Selection(lambda s: s._get_types(), required=True)
    login = fields.Char('Login')
    secret_key = fields.Char('Secret Key')
    template_ids = fields.One2many(
        'clouder.provider.template', 'name', 'Templates')

    @api.multi
    def _get_types(self):
        return [
            ('instance', 'Instance'), ('container', 'Container'),
            ('dns', 'DNS'), ('load', 'Load Balancing'), ('backup', 'Backup')]