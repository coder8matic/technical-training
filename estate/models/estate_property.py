# Tukaj definiramo model
# By convention all models are located in a models directory and each model is defined in its own Python file.
#
# resource
# https://www.odoo.com/documentation/master/developer/tutorials/server_framework_101/03_basicmodel.html

from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string='Name', required=True)                # Equivalent to character varying
    description = fields.Text(string='Description')  # Equivalent to text
    postcode = fields.Char(string='Postcode')        # Equivalent to character varying
    date_availability = fields.Date(string='Available From', copy=False, default=fields.Date.add(fields.Date.today(), months=3) )  # Equivalent to date
    expected_price = fields.Float(string='Expected Price' )    # Equivalent to double precision
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)      # Equivalent to double precision Copy=False; do not copy fields when copy document
    bedrooms = fields.Integer(string='Bedrooms', default=2)   # Equivalent to integer
    living_area = fields.Integer(string='Living Area (sqm)')  # Equivalent to integer
    facades = fields.Integer(string='Number of Facades')      # Equivalent to integer
    garage = fields.Boolean(string='Garage Available')        # Equivalent to boolean
    garden = fields.Boolean(string='Garden Available')        # Equivalent to boolean
    garden_area = fields.Integer(string='Garden Area (sqm)')  # Equivalent to integer
    garden_orientation = fields.Selection([                  # Equivalent to character varying
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation')
    active = fields.Boolean(string='Active', default=True)    # Equivalent to boolean
    state = fields.Selection([                               # Equivalent to character varying
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled')
    ], 
        string='State', 
        default='new',
        copy=False,
        required=True
    )
    # Relational Fields
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')  # Equivalent to integer
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)  # Equivalent to integer
    buyer_id = fields.Many2one('res.partner', string='Buyer' copy=False)  # Equivalent to integer
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')  # Equivalent to integer[]
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')  # Equivalent to integer[]

  

