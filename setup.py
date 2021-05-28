import pathlib
from setuptools import setup

with open("README.md","r") as fh:
	long_description = fh.read()

setup(
		name = 'roobet',
		version = '0.0.3',		
		author = 'Drew Nicolette',
		author_email = 'nicolettedrew0@gmail.com',
		description = 'Python library for querying Roobet Crash games',
		long_description = long_description,
        long_description_content_type='text/markdown',
		url="https://github.com/drewnicolette/roobet",
		license = 'MIT',
		packages = ['roobet'],
		zip_safe = False,
		include_package_data=True,
		install_requires=[],
      	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	)