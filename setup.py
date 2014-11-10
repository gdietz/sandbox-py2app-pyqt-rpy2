from setuptools import setup

setup(
  app=["mac_prelaunch.py"],
  options={"py2app":
    {"argv_emulation": True,
     "resources": ["/opt/local/Library/Frameworks/R.framework/Versions/Current/Resources",]}
     #"includes": ["sip", "PyQt4._qt"]}
     
  },
  setup_requires=["py2app"]) 