from setuptools import setup

setup(
  app=["main.py"],
  options={"py2app":
    {"argv_emulation": True,
     "resources": ["/opt/local/Library/Frameworks/R.framework/Versions/3.0/Resources",]}
     #"includes": ["sip", "PyQt4._qt"]}
     
  },
  setup_requires=["py2app"]) 