from setuptools import setup, find_namespace_packages

PROJECT = "log-viewer"

with open("requirements.txt", "r") as f:
    REQUIREMENTS = f.read().splitlines()
setup(
    name=PROJECT,
    version="0.0.1",
    description=f"{PROJECT} -> MONITOR LOG VIEWER",
    url=f"https://github.com/luongtt/{PROJECT}",
    author="luongtt",
    author_email="luongtt.it@gmail.com",
    python_requires='>=3.8',
    include_package_data=True,
    packages=find_namespace_packages(include=["web*"]),
    install_requires=REQUIREMENTS
)
