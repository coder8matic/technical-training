from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float(string='Price') # Equivalent to double precision
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='Status', 
       copy=False
    )
    property_id = fields.Many2one('estate.property', string='Property', required=True) # Equivalent to integer
    partner_id = fields.Many2one('res.partner', string='Partner', required=True) # Equivalent to integer