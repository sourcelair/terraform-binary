#!/usr/bin/env python

from setuptools import setup

TERRAFORM_VERSION = "0.11.8"

RELEASE_VERSION = "2"

__version__ = f"{TERRAFORM_VERSION}.post{RELEASE_VERSION}"

setup(
    name="terraform-binary",
    version=__version__,
    description="Python wrapper for Terraform",
    author="Paris Kasidiaris",
    author_email="paris@sourcelair.com",
    url="https://github.com/sourcelair/terraform-binary/",
    packages=["terraform"],
    package_dir={"teraform": "terraform"},
    package_data={"terraform": "lib/*"},
    entry_points={
        "console_scripts": [
            "terraform = terraform.terraform:main",
            "tf-binary-download = terraform.terraform:download",
        ]
    },
)
