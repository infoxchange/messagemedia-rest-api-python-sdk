# coding: utf-8

"""
    MessageMedia REST API

    Australia's Leading Messaging Solutions for Business and Enterprise.

    OpenAPI spec version: 1.0.0
    Contact: support@messagemedia.com

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import messagemedia_restapi
from messagemedia_restapi.rest import ApiException
from messagemedia_restapi.models.reporting_detail_properties import ReportingDetailProperties


class TestReportingDetailProperties(unittest.TestCase):
    """ ReportingDetailProperties unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReportingDetailProperties(self):
        """
        Test ReportingDetailProperties
        """
        model = messagemedia_restapi.models.reporting_detail_properties.ReportingDetailProperties()


if __name__ == '__main__':
    unittest.main()