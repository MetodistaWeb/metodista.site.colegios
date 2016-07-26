# -*- coding: utf-8 -*-
import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles

from metodista.site.colegios.testing import INTEGRATION_TESTING


class DefaultTest(unittest.TestCase):
    """ Test Case for Initial structure profile.
    """

    layer = INTEGRATION_TESTING

    def setUpUser(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

    def setUp(self):
        self.portal = self.layer['portal']
        self.setUpUser()
