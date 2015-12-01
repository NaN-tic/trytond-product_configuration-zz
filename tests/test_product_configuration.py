# This file is part of the product_configuration module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductConfigurationTestCase(ModuleTestCase):
    'Test Product Configuration module'
    module = 'product_configuration'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductConfigurationTestCase))
    return suite