# Tukaj definiramo model
# By convention all models are located in a models directory and each model is defined in its own Python file.
#
# resource
# https://www.odoo.com/documentation/master/developer/tutorials/server_framework_101/03_basicmodel.html

from odoo import models

class TestModel(models.Model):
    _name = "estate_property"
    _description = "Estate Property"

    # name = fields.Char(string='Title', required=True)
    id = fields.Integer(string='ID', required=True)
    create_uid = fields.Integer(intiger='create UID', required=false)
    

