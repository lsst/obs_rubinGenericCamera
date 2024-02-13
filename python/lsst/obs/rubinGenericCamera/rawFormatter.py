__all__ = ["StarTrackerNarrwRawFormatter", "StarTrackerWideRawFormatter", "StarTrackerFastRawFormatter",]

from .translator import StarTrackerNarrwTranslator, StarTrackerWideTranslator, StarTrackerFastTranslator
from lsst.obs.base import FitsRawFormatterBase
from .filters import RUBIN_GENERIC_CAMERA_FILTER_DEFINITIONS
from ._instrument import StarTrackerNarrw, StarTrackerWide, StarTrackerFast


class RubinGenericCameraRawFormatter(FitsRawFormatterBase):
    cameraClass = None
    translatorClass = None
    filterDefinitions = RUBIN_GENERIC_CAMERA_FILTER_DEFINITIONS

    def getDetector(self, id):
        return self.cameraClass().getCamera()[id]


class StarTrackerNarrwRawFormatter(RubinGenericCameraRawFormatter):
    cameraClass = StarTrackerNarrw
    translatorClass = StarTrackerNarrwTranslator


class StarTrackerWideRawFormatter(RubinGenericCameraRawFormatter):
    cameraClass = StarTrackerWide
    translatorClass = StarTrackerWideTranslator


class StarTrackerFastRawFormatter(RubinGenericCameraRawFormatter):
    cameraClass = StarTrackerFast
    translatorClass = StarTrackerFastTranslator
