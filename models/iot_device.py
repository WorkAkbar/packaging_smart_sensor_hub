#  Model perangkat IoT 
from odoo import models, fields

class IoTDevice(models.Model):
    _name = 'iot.device'
    _description = 'IoT Device'

    name = fields.Char(string='Device Name', required=True)
    device_type = fields.Selection([
        ('sensor', 'Sensor'),
        ('camera', 'Camera'),
    ], string='Device Type', required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active')
    location = fields.Char(string='Location')

