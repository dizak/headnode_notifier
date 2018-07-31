from setuptools import setup, find_packages
from headnode_notifier import __version__ as VERSION
from headnode_notifier import __author__ as AUTHOR


setup(
    name="headnode_notifier",
    version=VERSION,
    author=AUTHOR,
    packages=find_packages(exclude=["*test*"]),
    install_requires=open("requirements.txt").readlines(),
    description="Simple script for sending emails",
    author_email="dariusz.izak@ibb.waw.pl",
    url="https://github.com/dizak/headnode_notifier",
    license="MIT",
    py_modules=["headnode_notifier"],
    scripts=["headnode_notifier.py"],
    keywords=[
        "smtp",
        "script",
        "mail",
        "client",
        "layer",
    ],
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ]
)
