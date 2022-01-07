from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_firebase/__init__.py
from frappe_firebase import __version__ as version

setup(
	name="frappe_firebase",
	version=version,
	description="A simple custom firebase app for frappe",
	author="Vinay Rawat",
	author_email="vineyrawat@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
