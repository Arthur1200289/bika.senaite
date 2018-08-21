# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from senaite.bikaimages.testing import SENAITE_BIKAIMAGES_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that senaite.bikaimages is properly installed."""

    layer = SENAITE_BIKAIMAGES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if senaite.bikaimages is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'senaite.bikaimages'))

    def test_browserlayer(self):
        """Test that ISenaiteBikaimagesLayer is registered."""
        from senaite.bikaimages.interfaces import (
            ISenaiteBikaimagesLayer)
        from plone.browserlayer import utils
        self.assertIn(ISenaiteBikaimagesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SENAITE_BIKAIMAGES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['senaite.bikaimages'])

    def test_product_uninstalled(self):
        """Test if senaite.bikaimages is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'senaite.bikaimages'))

    def test_browserlayer_removed(self):
        """Test that ISenaiteBikaimagesLayer is removed."""
        from senaite.bikaimages.interfaces import \
            ISenaiteBikaimagesLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISenaiteBikaimagesLayer, utils.registered_layers())
