"""Tests of the RubinGenericCamera instrument class.
"""

import unittest

import lsst.utils.tests
import lsst.obs.rubinGenericCamera
from lsst.obs.base.instrument_tests import InstrumentTests, InstrumentTestData


class TestStarTrackerNarrow(InstrumentTests, lsst.utils.tests.TestCase):
    def setUp(self):
        physical_filters = set(["empty"])

        self.data = InstrumentTestData(name="StarTrackerNarrow",
                                       nDetectors=1,
                                       firstDetectorName="CCD0",
                                       physical_filters=physical_filters)
        self.instrument = lsst.obs.rubinGenericCamera.StarTrackerNarrow()


class TestStarTrackerWide(InstrumentTests, lsst.utils.tests.TestCase):
    def setUp(self):
        physical_filters = set(["empty"])

        self.data = InstrumentTestData(name="StarTrackerWide",
                                       nDetectors=1,
                                       firstDetectorName="CCD0",
                                       physical_filters=physical_filters)
        self.instrument = lsst.obs.rubinGenericCamera.StarTrackerWide()


class TestStarTrackerFast(InstrumentTests, lsst.utils.tests.TestCase):
    def setUp(self):
        physical_filters = set(["empty"])

        self.data = InstrumentTestData(name="StarTrackerFast",
                                       nDetectors=1,
                                       firstDetectorName="CCD0",
                                       physical_filters=physical_filters)
        self.instrument = lsst.obs.rubinGenericCamera.StarTrackerFast()


if __name__ == '__main__':
    lsst.utils.tests.init()
    unittest.main()
