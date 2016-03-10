# This file is part product_configuration module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton
from trytond.pool import Pool
from trytond.transaction import Transaction

from sql import Literal


__all__ = ['Configuration']


class Configuration(ModelSingleton, ModelSQL, ModelView):
    'Product Configuration'
    __name__ = 'product.configuration'

    @classmethod
    def __register__(cls, module_name):
        # Module deprecated since version 4.0
        # Uninstall module when update database if installed
        pool = Pool()
        Module = pool.get('ir.module')

        cursor = Transaction().connection.cursor()
        module = Module.__table__()

        cursor.execute(*module.update(
                columns=[module.state],
                values=[Literal('to remove')],
                where=module.name == Literal('product_configuration')
                ))

        super(Configuration, cls).__register__(module_name)
