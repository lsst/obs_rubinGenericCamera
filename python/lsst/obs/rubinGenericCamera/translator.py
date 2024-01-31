import os

import numpy as np
import astropy.units as u
from astropy.time import Time

from astro_metadata_translator import cache_translation
from lsst.obs.lsst.translators.lsst import LsstBaseTranslator

from lsst.utils import getPackageDir

__all__ = ["StarTrackerNarrwTranslator", "StarTrackerWideTranslator", "StarTrackerFastTranslator",]


class RubinGenericCameraTranslator(LsstBaseTranslator):
    """Metadata translator for Rubin Generic Camera FITS headers"""

    name = None                         # you must specialise this class
    """Name of this translation class"""

    supported_instrument = None         # you must specialise this class
    """Supports the LSST Generic Camera instrument."""

    default_search_path = os.path.join(getPackageDir("obs_rubinGenericCamera"), "corrections")
    """Default search path to use to locate header correction files."""

    default_resource_root = os.path.join(getPackageDir("obs_rubinGenericCamera"), "corrections")
    """Default resource path root to use to locate header correction files."""

    DETECTOR_MAX = 1

    _const_map = {"detector_num": 0,
                  "boresight_rotation_coord": "sky",
                  "physical_filter": "empty",
                  "detector_group": "None",
                  "relative_humidity": None,
                  "pressure": None,
                  "temperature": None,
                  "focus_z": None,
                  }
    """Constant mappings"""

    _trivial_map = {
        "boresight_rotation_angle": (["ROTPA", "ROTANGLE"], dict(default=np.NaN, unit=u.deg)),
        "detector_name": "CAMMM",
        "object": ("OBJECT", dict(default="UNKNOWN")),
        "observation_id": "OBSID",
        "observation_type": "IMGTYPE",
        "science_program": ("PROGRAM", dict(default="unknown")),
        "telescope": "TELESCOP",
    }
    """One-to-one mappings"""

    extensions = dict(
    )

    @classmethod
    def can_translate(cls, header, filename=None):
        """Indicate whether this translation class can translate the
        supplied header.

        Parameters
        ----------
        header : `dict`-like
            Header to convert to standardized form.
        filename : `str`, optional
            Name of file being translated.

        Returns
        -------
        can : `bool`
            `True` if the header is recognized by this class. `False`
            otherwise.
        """

        return False                    # you must specialise this class

    @cache_translation
    def to_datetime_begin(self):
        self._used_these_cards("MJD-BEG")
        return Time(self._header["MJD-BEG"], scale="tai", format="mjd")

    @cache_translation
    def to_instrument(self):
        return None                     # you must specialise this class

    @cache_translation
    def to_exposure_time(self):
        # Docstring will be inherited. Property defined in properties.py
        # Some data is missing a value for EXPTIME.
        # Have to be careful we do not have circular logic when trying to
        # guess
        if self.is_key_ok("EXPTIME"):
            return self.quantity_from_card("EXPTIME", u.s)

        # A missing or undefined EXPTIME is problematic. Set to -1
        # to indicate that none was found.
        self.log.warning("%s: Insufficient information to derive exposure time. Setting to -1.0s",
                         self._log_prefix)
        return -1.0 * u.s

    @cache_translation
    def to_dark_time(self):             # N.b. defining this suppresses a warning re setting from exptime
        if "DARKTIME" in self._header:
            darkTime = self._header["DARKTIME"]
            self._used_these_cards("DARKTIME")
            return (darkTime, dict(unit=u.s))
        return self.to_exposure_time()


class StarTrackerTranslator(RubinGenericCameraTranslator):
    name = None                         # must be specialised
    """Name of this translation class"""

    supported_instrument = None         # must be specialised
    """Supports the Rubin Star Tracker instrument."""

    @classmethod
    def _is_startracker(cls, header, filename=None):
        """Indicate whether the supplied header comes from a starTracker

        Parameters
        ----------
        header : `dict`-like
            Header to convert to standardized form.
        filename : `str`, optional
            Name of file being translated.

        Returns
        -------
        (isStarTracker, camId) : (`True`, `int`) or (`False`, `None`)
            isStarTracker is `True` iff header comes from a starTracker
            camId is the cameraID, e.g. 101 for the wide-field startracker,
            102 for the narrow-field startracker
        """
        if "INSTRUME" not in header or header["INSTRUME"] != "StarTracker" or "OBSID" not in header:
            return (False, None)

        camId = int(header["OBSID"][2:5])

        return (True, camId)


class StarTrackerNarrwTranslator(StarTrackerTranslator):
    name = "StarTrackerNarrw"
    """Name of this translation class"""

    supported_instrument = "StarTrackerNarrw"
    """Supports the Rubin Star Tracker narrow-field instrument."""

    @classmethod
    def can_translate(cls, header, filename=None):
        """Indicate whether this translation class can translate the
        supplied header.

        Parameters
        ----------
        header : `dict`-like
            Header to convert to standardized form.
        filename : `str`, optional
            Name of file being translated.

        Returns
        -------
        can : `bool`
            `True` if the header is recognized by this class. `False`
            otherwise.
        """

        isStarTracker, camId = cls._is_startracker(header, filename=None)

        return isStarTracker and camId == 102

    @cache_translation
    def to_instrument(self):
        return "StarTrackerNarrw"

    @cache_translation
    def to_detector_serial(self):
        return "00:0f:31:03:ae:60"


class StarTrackerWideTranslator(StarTrackerTranslator):
    name = "StarTrackerWide"
    """Name of this translation class"""

    supported_instrument = "StarTrackerWide"
    """Supports the Rubin Star Tracker wide-field instrument."""

    @classmethod
    def can_translate(cls, header, filename=None):
        """Indicate whether this translation class can translate the
        supplied header.

        Parameters
        ----------
        header : `dict`-like
            Header to convert to standardized form.
        filename : `str`, optional
            Name of file being translated.

        Returns
        -------
        can : `bool`
            `True` if the header is recognized by this class. `False`
            otherwise.
        """
        isStarTracker, camId = cls._is_startracker(header, filename=None)

        return isStarTracker and camId == 101

    @cache_translation
    def to_instrument(self):
        return "StarTrackerWide"

    @cache_translation
    def to_detector_serial(self):
        return "00:0f:31:03:60:c2"      # MAC address

class StarTrackerFastTranslator(StarTrackerTranslator):
    name = "StarTrackerFast"
    """Name of this translation class"""

    supported_instrument = "starTrackerFast"
    """Supports the STARTRACKERFAST dome-seeing instrument."""

    @classmethod
    def can_translate(cls, header, filename=None):
        """Indicate whether this translation class can translate the
        supplied header.

        Parameters
        ----------
        header : `dict`-like
            Header to convert to standardized form.
        filename : `str`, optional
            Name of file being translated.

        Returns
        -------
        can : `bool`
            `True` if the header is recognized by this class. `False`
            otherwise.
        """
        isStarTracker, camId = cls._is_startracker(header, filename=None)

        return isStarTracker and camId == 103

    @cache_translation
    def to_instrument(self):
        return "StarTrackerFast"

    @cache_translation
    def to_detector_serial(self):
        return "00:0F:31:03:3F:BA"    # MAC address
