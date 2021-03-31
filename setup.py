from setuptools import find_packages, setup

setup(
    name="tiktok-dl",
    version="1.0.0",
    description="Allows you to download TikTok Videos as MP4",
    install_requires=["beautifulsoup4", "requests", "argparse"],
    entry_points = {
        "console_scripts": ["tiktok-dl=tiktokdl.cli:main"]
    }
)
