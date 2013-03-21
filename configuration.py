# This file is part product_configuration module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.pool import Pool
from trytond.transaction import Transaction

__all__ = [
    'ProductConfiguration',
    'ProductConfigurationCompany',
]


class ProductConfiguration(ModelSingleton, ModelSQL, ModelView):
    'Product Configuration'
    __name__ = 'product.configuration'
    company = fields.Function(fields.Many2One('company.company','Company', 
        readonly=True), 'get_fields', setter='set_fields')

    @classmethod
    def get_fields(cls, configurations, names):
        res = {}
        ConfigurationCompany = Pool().get('product.configuration.company')
        company_id = Transaction().context.get('company')
        conf_id = configurations[0].id
        if company_id:
            confs = ConfigurationCompany.search([
                ('company', '=', company_id),
                ], limit=1)
            for conf in confs:
                for field_name in names:
                    value = getattr(conf, field_name)
                    if value and (not isinstance(value, unicode) 
                        and not isinstance(value, int)):
                            value = value.id
                    res[field_name] = {conf_id: value}
        return res

    @classmethod
    def set_fields(cls, configurations, name, value):
        if value:
            ConfigurationCompany = Pool().get('product.configuration.company')
            company_id = Transaction().context.get('company')
            if company_id:
                configuration = ConfigurationCompany.search([
                    ('company', '=', company_id),
                    ], limit=1)
                if not configuration:
                    vlist = [{
                            'company': company_id,
                            name: value,
                            }]
                    ConfigurationCompany.create(vlist)
                else:
                    ConfigurationCompany.write([configuration[0]],
                                                 {name: value})


class ProductConfigurationCompany(ModelSQL, ModelView):
    'Product Configuration Company'
    __name__ = 'product.configuration.company'
    company = fields.Many2One('company.company', 'Company',
        required=True, readonly=True)

    @classmethod
    def __setup__(cls):
        super(ProductConfigurationCompany, cls).__setup__()
        cls._sql_constraints += [
            ('company_uniq', 'UNIQUE(company)',
                'There is already one configuration for this company.'),
        ]
