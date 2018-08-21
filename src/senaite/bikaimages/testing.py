# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import senaite.bikaimages


class SenaiteBikaimagesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=senaite.bikaimages)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'senaite.bikaimages:default')


SENAITE_BIKAIMAGES_FIXTURE = SenaiteBikaimagesLayer()


SENAITE_BIKAIMAGES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SENAITE_BIKAIMAGES_FIXTURE,),
    name='SenaiteBikaimagesLayer:IntegrationTesting'
)


SENAITE_BIKAIMAGES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SENAITE_BIKAIMAGES_FIXTURE,),
    name='SenaiteBikaimagesLayer:FunctionalTesting'
)


SENAITE_BIKAIMAGES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SENAITE_BIKAIMAGES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='SenaiteBikaimagesLayer:AcceptanceTesting'
)
