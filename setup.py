import setuptools
import os

with open("README.md","r",encoding='utf-8')as f:
    long_description=f.read()


__version__="0.0.0"
REPO_NAME="Chicken_Disease_classifier"
SOURCE_REPO_NAME="CHICKEN_DISEASE_CLASSIFIER"
AUTHOR_ID="girish12ns"
EMAIL_ID="girish12n@gmail.com"


setuptools.setup(
    version=__version__,  
    name=SOURCE_REPO_NAME,
    author=AUTHOR_ID,
    author_email=EMAIL_ID,
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/{AUTHOR_ID}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_ID}/{REPO_NAME}/issues",
    },

   package_dir={"":"src"},
   packages=setuptools.find_packages(where="src"))
