# -*- python -*-
from lsst.sconsUtils import scripts

# Force shebang and policy to come first so that camera geometry
# will guarantee to be complete before tests run.
targetList = ("version", "shebang", "policy",) + scripts.DEFAULT_TARGETS

scripts.BasicSConstruct("obs_rubinGenericCamera", disableCc=True, defaultTargets=targetList, noCfgFile=True)
