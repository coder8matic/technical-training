# Tukaj definiramo model
# By convention all models are located in a models directory and each model is defined in its own Python file.
#
# resource
# https://www.odoo.com/documentation/master/developer/tutorials/server_framework_101/03_basicmodel.html

from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    # Basic fields
    name = fields.Char(string='Name')                # Equivalent to character varying
    description = fields.Text(string='Description')  # Equivalent to text
    postcode = fields.Char(string='Postcode')        # Equivalent to character varying
    date_availability = fields.Date(string='Available From')  # Equivalent to date
    expected_price = fields.Float(string='Expected Price')    # Equivalent to double precision
    selling_price = fields.Float(string='Selling Price')      # Equivalent to double precision
    bedrooms = fields.Integer(string='Bedrooms')             # Equivalent to integer
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


  

