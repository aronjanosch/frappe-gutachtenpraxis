from frappe import _

def get_data():
    return {
        'fieldname': 'gutachten',
        'non_standard_fieldnames': {
            'Tagesliste': 'gutachten',
            'Termin': 'gutachten',
        },
        'transactions': [
            {
                'label': _('Verbundene Tagesliste'),
                'items': ['Tagesliste']
            },
            {
                'label': _('Verbundene Termine'),
                'items': ['Termin']
            },
        ]
    }
