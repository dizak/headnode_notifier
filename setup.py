from setuptools import setup
from headnode_notifier import __version__ as VERSION
from headnode_notifier import __author__ as AUTHOR


setup(name="headnode_notifier",
      version=VERSION,
      description="Simple script for sending emails",
      author=AUTHOR,
      author_email="dariusz.izak@ibb.waw.pl",
      url="https://github.com/dizak/headnode_notifier",
      license="MIT",
      py_modules=["headnode_notifier"],
      scripts=["headnode_notifier.py"])
