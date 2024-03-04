"""Unit tests for Gen3 RubinGC raw data ingest.
"""

import unittest
import os
import lsst.utils.tests

from lsst.obs.base.ingest_tests import IngestTestBase
from lsst.obs.rubinGenericCamera import StarTrackerWide, StarTrackerNarrow, StarTrackerFast
from lsst.obs.rubinGenericCamera.filters import RUBIN_GENERIC_CAMERA_FILTER_DEFINITIONS

testDataPackage = "obs_rubinGenericCamera"
try:
    testDataDirectory = lsst.utils.getPackageDir(testDataPackage)
except (LookupError, lsst.pex.exceptions.NotFoundError):
    testDataDirectory = None


@unittest.skipIf(testDataDirectory is None, "obs_rubinGenericCamera must be set up")
class StarTrackerNarrowIngestTestCase(IngestTestBase, lsst.utils.tests.TestCase):
    instrumentClassName = "lsst.obs.rubinGenericCamera.StarTrackerNarrow"

    visits = None                       # we don't have a definition of visits

    def setUp(self):
        self.ingestdir = os.path.dirname(__file__)
        self.instrument = StarTrackerNarrow()
        self.file = os.path.join(testDataDirectory, "data", "input", "raw", "GC102_O_20221208_000211.fits.gz")
        self.dataIds = [dict(instrument="StarTrackerNarrow", exposure=2022120800211, detector=0)]
        self.filterLabel = RUBIN_GENERIC_CAMERA_FILTER_DEFINITIONS[0].makeFilterLabel()

        super().setUp()


@unittest.skipIf(testDataDirectory is None, "obs_rubinGenericCamera must be set up")
class StarTrackerWideIngestTestCase(IngestTestBase, lsst.utils.tests.TestCase):
    instrumentClassName = "lsst.obs.rubinGenericCamera.StarTrackerWide"

    visits = None                       # we don't have a definition of visits

    def setUp(self):
        self.ingestdir = os.path.dirname(__file__)
        self.instrument = StarTrackerWide()
        self.file = os.path.join(testDataDirectory, "data", "input", "raw", "GC101_O_20221208_000211.fits.gz")
        self.dataIds = [dict(instrument="StarTrackerWide", exposure=2022120800211, detector=0)]
        self.filterLabel = RUBIN_GENERIC_CAMERA_FILTER_DEFINITIONS[0].makeFilterLabel()

        super().setUp()


@unittest.skipIf(testDataDirectory is None, "obs_rubinGenericCamera must be set up")
class StarTrackerFastIngestTestCase(IngestTestBase, lsst.utils.tests.TestCase):
    instrumentClassName = "lsst.obs.rubinGenericCamera.StarTrackerFast"

    visits = None                       # we don't have a definition of visits

    def setUp(self):
        self.ingestdir = os.path.dirname(__file__)
        self.instrument = StarTrackerFast()
        self.file = os.path.join(testDataDirectory, "data", "input", "raw", "GC103_O_20221208_000211.fits.gz")
        self.dataIds = [dict(instrument="StarTrackerFast", exposure=2022120800211, detector=0)]
        self.filterLabel = RUBIN_GENERIC_CAMERA_FILTER_DEFINITIONS[0].makeFilterLabel()

        super().setUp()


def setup_module(module):
    lsst.utils.tests.init()


if __name__ == "__main__":
    lsst.utils.tests.init()
    unittest.main()
