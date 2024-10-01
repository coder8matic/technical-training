from odoo import models, fields, api
import datetime

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    _order = 'price desc'

    property_id = fields.Many2one('estate.property', string='Property ID', required=True) # Equivalent to integer
    price = fields.Float(string='Price') # Equivalent to double precision
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='Status', 
       copy=False
    )
    
    # computed field
    date_deadline = fields.Datetime(string='Date')
    @api.depends("date_deadline")
    def _compute_date_deadline(self):
        for date in self:
            date.date_deadline = datetime.datetime.now() + datetime.timedelta(days=7)
    def _inverse_total(self):
        for date in self:
            date.date_deadline = datetime.datetime.now() #+ datetime.timedelta(days=7)

    # Relations
    partner_id = fields.Many2one('res.partner', string='Partner', required=True) # Equivalent to integer
    