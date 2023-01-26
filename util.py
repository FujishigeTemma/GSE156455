import os
from urllib.parse import urlparse
from ftplib import FTP
from typing import Callable
import gzip
import shutil


def download_all_data_if_not_exist(url: str, dst: str, filter: Callable[[str], bool] = lambda abspath: True):
    """
    Download data if not exist via FTP.

    Args:
      url: FTP url must contain hostname and dir path.
      dst: destination path where files downloaded. If not exist, it will be created.
      filter: filter function to filter files.
    """
    os.makedirs(dst, exist_ok=True)
    parsed = urlparse(url)
    if parsed.hostname is None:
        raise ValueError(f"Invalid URL: {url}")
    ftp = FTP(parsed.hostname)
    ftp.login()

    files = ftp.nlst(parsed.path)
    if len(files) == 0:
        raise ValueError(f"No such file or directory: {parsed.path}")
    files = [file for file in files if filter(file)]

    for file in files:
        filename = os.path.basename(file)
        if not os.path.isfile(os.path.join(dst, filename)):
            with open(os.path.join(dst, filename), "wb+") as f:
                ftp.retrbinary("RETR " + file, f.write)
            print("Downloaded:", file)
        else:
            print(f"File already exists: {filename} in {dst}")


def unzip(src: str, dst: str):
    """
    Unzip all files in src directory to dst.
    """
    for file in os.listdir(src):
        if file.endswith(".gz") and not os.path.isfile(os.path.join(dst, file.removesuffix(".gz"))):
            with gzip.open(os.path.join(src, file), "rb") as f_in:
                with open(os.path.join(dst, file), "wb+") as f_out:
                    shutil.copyfileobj(f_in, f_out)
