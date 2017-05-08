from distutils.core import setup
from headnode_notifier import __version__ as version

setup(name="headnode_notifier",
      version=version,
      scripts=["headnode_notifier.py"])
