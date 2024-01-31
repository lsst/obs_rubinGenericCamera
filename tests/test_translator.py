# This file is part of obs_rubinGenericCamera.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import unittest
import astropy.units as u
import astropy.units.cds as cds
import lsst.obs.lsst.translators  # noqa: F401 -- register the translators
from lsst.obs.rubinGenericCamera.translator import StarTrackerNarrwTranslator, \
    StarTrackerWideTranslator, StarTrackerFastTranslator

from astro_metadata_translator.tests import MetadataAssertHelper

TESTDIR = os.path.abspath(os.path.dirname(__file__))


class RubinGenericCameraMetadataTranslatorTestCase(unittest.TestCase, MetadataAssertHelper):
    """Each test reads in raw headers from YAML files, constructs an
    `ObservationInfo`, and compares the properties with the expected values
    defined in the corresponding `dict`."""

    datadir = os.path.join(TESTDIR, "headers")

    def test_comCam_translator(self):
        test_data = [
            ("GC101_O_20221208_000211.yaml",
             dict(telescope="Simonyi Survey Telescope",
                  instrument="StarTrackerWide",
                  boresight_rotation_coord="sky",
                  dark_time=5.0*u.s,
                  detector_group="None",
                  detector_name="AlliedVision GT3300",
                  detector_num=0,
                  detector_serial="00:0f:31:03:60:c2",
                  exposure_id=2022120800211,
                  exposure_group="2022-12-09T05:20:47.840",
                  exposure_time=5.0*u.s,
                  group_counter_start=212,
                  group_counter_end=212,
                  object="UNKNOWN",
                  observation_counter=211,
                  observation_id="GC101_O_20221208_000211",
                  observation_type="OBJECT",
                  observation_reason="lvv-t2730 lvv-exxxx",
                  observing_day=20221208,
                  physical_filter="empty",
                  pressure=None,
                  relative_humidity=None,
                  science_program="",
                  temperature=None,
                  )),
            ("GC102_O_20221208_000211.yaml",
             dict(telescope="Simonyi Survey Telescope",
                  instrument="StarTrackerNarrw",
                  boresight_rotation_coord="sky",
                  dark_time=3.0*u.s,
                  detector_group="None",
                  detector_name="AlliedVision GT3400",
                  detector_num=0,
                  detector_serial="00:0f:31:03:ae:60",
                  exposure_id=2022120800211,
                  exposure_group="2022-12-09T05:20:47.841",
                  exposure_time=3.0*u.s,
                  group_counter_start=212,
                  group_counter_end=212,
                  object="UNKNOWN",
                  observation_counter=211,
                  observation_id="GC102_O_20221208_000211",
                  observation_type="OBJECT",
                  observation_reason="lvv-t2730 lvv-exxxx",
                  observing_day=20221208,
                  physical_filter="empty",
                  pressure=None,
                  relative_humidity=None,
                  science_program="",
                  temperature=None,
                  )),
            ("GC103_O_20221208_000211.yaml",
             dict(telescope="Simonyi Survey Telescope",
                  instrument="StarTrackerFast",
                  boresight_rotation_coord="sky",
                  dark_time=0.1*u.s,
                  detector_group="None",
                  detector_name="AlliedVision GC650M",
                  detector_num=0,
                  detector_serial="00:0F:31:03:3F:BA",
                  exposure_id=2022120800211,
                  exposure_group="2022-12-09T05:20:47.842",
                  exposure_time=0.1*u.s,
                  group_counter_start=212,
                  group_counter_end=212,
                  object="UNKNOWN",
                  observation_counter=211,
                  observation_id="GC103_O_20221208_000211",
                  observation_type="OBJECT",
                  observation_reason="lvv-t2730 lvv-exxxx",
                  observing_day=20221208,
                  physical_filter="empty",
                  pressure=None,
                  relative_humidity=None,
                  science_program="",
                  temperature=None,
                  )),
        ]
        for filename, expected in test_data:
            with self.subTest(f"Testing {filename}"):
                self.assertObservationInfoFromYaml(filename, dir=self.datadir, **expected)


if __name__ == "__main__":
    unittest.main()
