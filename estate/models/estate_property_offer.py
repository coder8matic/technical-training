from odoo import models, fields

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
    partner_id = fields.Many2one('res.partner', string='Partner', required=True) # Equivalent to integer
    