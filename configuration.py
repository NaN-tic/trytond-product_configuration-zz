# This file is part product_configuration module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.pool import Pool
from trytond.transaction import Transaction

__all__ = ['Configuration']


class Configuration(ModelSingleton, ModelSQL, ModelView):
    'Product Configuration'
    __name__ = 'product.configuration'

