# -*- coding: utf-8 -*-

{
    'name': 'Odoo18 Employee Contracts Types',
    'version': '18.0.1.0.0',
    'category': 'Generic Modules/Human Resources',
    'summary': """
        Contract type in contracts
    """,
    'description': """Employee category (type_id) on contracts. Since 15.0 the
contract types (hr.contract.type) are part of Odoo (Employees > Configuration >
Employment Types): this module only keeps the "Employee Category" of the contract.""",
    'author': 'Odoo SA,Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['hr', 'hr_contract'],
    'data': [
        'views/contract_view.xml',
    ],
    'installable': True,
    'images': ['static/description/banner.png'],
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
