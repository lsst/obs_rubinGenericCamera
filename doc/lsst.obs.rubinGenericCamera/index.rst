.. py:currentmodule:: lsst.obs.rubinGenericCamera

.. _lsst.obs.rubinGenericCamera:

###########################
lsst.obs.rubinGenericCamera
###########################

The ``obs_rubinGenericCamera`` module defines Rubin generic camera specific configurations.

.. Add subsections with toctree to individual topic pages.

.. _lsst.obs.lsst-contributing:

Using the Package Ab Initio
===========================

If you have some data but no ``butler`` (not a typical situation, but one facing the developers
of new obs-packages), these are the steps required to get as far as running the ISR.

Start with some environment variables (my data's at USDF), and a list of the instruments to process:

.. code-block:: sh

   DATA=~rlupton/Data/RubinGenericCamera	# N.b. I own this data, and you shouldn't have to write to it
   REPO=~/Repo/RubinGenericCamera		# N.b. not ~rlupton -- you own this file
   LABEL="rhl-scr"
   COLLBASE=u/rhl/tmp

   instruments="StarTrackerNarrow StarTrackerWide StarTrackerFast"


Clean up from previous attempts and initialise the ``butler``
(in reality, I chain these blocks together with ``&&``)

.. code-block:: sh

   rm -rf $REPO &&
   butler create $REPO &&
   obs_package=rubinGenericCamera &&
   for inst in $instruments; do
      butler register-instrument $REPO lsst.obs.$obs_package.$inst &&
      butler write-curated-calibrations $REPO --label $LABEL $inst &&
      butler collection-chain $REPO --mode redefine $inst/calib \
	       $inst/calib/$LABEL $inst/calib/$LABEL/unbounded
   done

Ingest the raw data

.. code-block:: sh

   butler ingest-raws $REPO $DATA/raw/10[123]

and run the pipelines

.. code-block:: sh

   for inst in $instruments; do
      pipetask run -b $REPO -i $inst/raw/all,$inst/calib \
	     -o "$COLLBASE-$inst" \
	     -d "instrument='$inst' AND exposure.day_obs=20221208 AND exposure.seq_num=211" \
	     -p $OBS_RUBINGENERICCAMERA_DIR/pipelines/$inst/ISR.yaml --register-dataset-types
   done
   
Contributing
============

``lsst.obs.rubinGenericCamera`` is developed at https://github.com/lsst/obs_rubinGenericCamera.
You can find Jira issues for this module under the `obs_rubinGenericCamera <https://jira.lsstcorp.org/issues/?jql=project%20%3D%20DM%20AND%20component%20%3D%20obs_rubinGenericCamera>`_ component.

.. toctree::
   :maxdepth: 1

   testing.rst

.. _lsst.obs.lsst-pyapi:

Python API reference
====================

.. automodapi:: lsst.obs.rubinGenericCamera
   :no-main-docstr:
.. automodapi:: lsst.obs.rubinGenericCamera.translator
   :no-main-docstr:
