from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["pyphone=pyphone:main", ]
    },
    python_requires='~=3.5',
    install_requires=["python-gammu", "Pillow", "httplib2", "oauth2client", "google-api-python-client", "pyperclip"],

    name="pyPhone",
    version="1.0.0a1",
    description="Minimalistic phone client",
    long_description=long_description,
    author="Christopher Hubmann",
    author_email="christopher.hubmann@gmail.com",
    platforms=["Linux", "Mac OSX", "Windows XP/2000/NT", "Windows 95/98/ME"],
    keywords=[
        "mobile", "phone", "SMS", "gammu", "google", "contacts"
    ],
    license="MIT",
    url="https://github.com/ChrisDeadman/pyPhone",
    download_url="https://github.com/ChrisDeadman/pyPhone/archive/master.zip",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved"
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Topic :: Utilities",
        "Topic :: Communications :: Telephony",
        "Topic :: System :: Hardware"
    ]
)
