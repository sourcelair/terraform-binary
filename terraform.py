"""Python wrapper for Hashicorp's Terraform pre-built binary."""

import os
import stat
import sys
import urllib.request
import zipfile
import platform


BASE_DIR = os.path.dirname(__file__)
TERRAFORM_VERSION = "0.12.5"
TERRAFORM_EXECUTABLE_SYSTEM = os.path.join(sys.prefix, 'lib/terraform')
TERRAFORM_EXECUTABLE_LOCAL = os.path.join(BASE_DIR, 'lib/terraform')
TERRAFORM_EXECUTABLE = (
    TERRAFORM_EXECUTABLE_SYSTEM
    if os.path.exists(TERRAFORM_EXECUTABLE_SYSTEM)
    else TERRAFORM_EXECUTABLE_LOCAL
)


def download(version=TERRAFORM_VERSION):
    platform_name = platform.system().lower()
    base_url = f"https://releases.hashicorp.com/terraform/{version}"
    file_name = f"terraform_{version}_{platform_name}_amd64.zip"
    download_url = f"{base_url}/{file_name}"

    download_directory = "downloads"
    extract_directory = "lib"
    target_file = f"{download_directory}/{file_name}"

    os.makedirs(download_directory, exist_ok=True)
    os.makedirs(extract_directory, exist_ok=True)

    urllib.request.urlretrieve(download_url, target_file)

    with zipfile.ZipFile(target_file) as terraform_zip_archive:
        terraform_zip_archive.extractall(extract_directory)

    executable_path = f"{extract_directory}/terraform"
    executable_stat = os.stat(executable_path)
    os.chmod(executable_path, executable_stat.st_mode | stat.S_IEXEC)


def main():
    args = [] if len(sys.argv) < 2 else sys.argv[1:]
    os.execv(TERRAFORM_EXECUTABLE, ["terraform"] + args)
