.. _obs_lsst_testing:

Testing the Package
===================

Unit Tests
----------

The unit tests for this package consist of butler (ingestion and instrument) tests for each camera,
and metadata translation tests.

Butler Tests
^^^^^^^^^^^^

The butler tests use the testing infrastructure from `lsst.obs.base` and there
are test cases for each camera in ``tests/test_ingestion.py`` and ``tests/test_instrument.py``.

Metadata Translation
^^^^^^^^^^^^^^^^^^^^

The `astro_metadata_translator` header translators (currently defined in `lsst.obs.lsst.translators`) are tested in ``tests/test_translator.py``.
There is a test method per camera and the reference headers are stored as YAML files in ``tests/headers``.
YAML is used to simplify the movement of these tests into `astro_metadata_translator` at some point in the future.
A header file can be generated in this format by running:

.. code-block:: bash

   astrometadata dump myTestfile.fits > tests/headers/myTestfile.yaml
