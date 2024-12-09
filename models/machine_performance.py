from odoo import models, fields, api

class MachinePerformance(models.Model):
    _name = 'machine.performance'
    _description = 'Machine Performance'

    device_id = fields.Many2one('iot.device', string='Device')
    temperature = fields.Float(string='Temperature (°C)')
    pressure = fields.Float(string='Pressure (Pa)')
    speed = fields.Float(string='Speed (RPM)')
    timestamp = fields.Datetime(string='Timestamp', default=fields.Datetime.now)
