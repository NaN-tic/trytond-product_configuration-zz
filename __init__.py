#This file is part product_configuration module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

from trytond.pool import Pool
from .configuration import *

def register():
    Pool.register(
        ProductConfiguration,
        ProductConfigurationCompany,
        module='product_configuration', type_='model')
