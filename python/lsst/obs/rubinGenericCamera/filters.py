from lsst.obs.base import FilterDefinition, FilterDefinitionCollection

RUBIN_GENERIC_CAMERA_FILTER_DEFINITIONS = FilterDefinitionCollection(
    FilterDefinition(band="white", physical_filter="empty"),
)
