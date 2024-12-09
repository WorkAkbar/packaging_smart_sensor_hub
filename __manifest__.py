
# __manifest__.py
{
    'name': 'Packaging Smart Sensor Hub',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'IoT-based monitoring and optimization for packaging production',
    'author': 'akbar',
    'website': 'https://www.yourwebsite.com',
    'depends': ['base', 'mrp'],  # Menggunakan modul Manufacturing (MRP)
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_views.xml'
        'views/iot_device_views.xml',
        'views/machine_performance_views.xml',
        'views/quality_check_views.xml',
        'data/iot_device_data.xml',  # Data default untuk perangkat IoT
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

