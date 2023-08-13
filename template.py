import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s - %(message)s]')




project_name="CHICKEN_DISEASE_CLASSIFIER"

directories_list=[
    ".github/workflows/.gitkeep",
    "src/{}/__init__.py".format(project_name),
    "src/{}/components/__init__.py".format(project_name),
    "src/{}/utils/__init__.py".format(project_name),
    "src/{}/config/__init__.py".format(project_name),
    "src/{}/config/configuration.py/".format(project_name),
    "src/{}/entity/__init__.py".format(project_name),
    "src/{}/constants/__init__.py".format(project_name),
    "src/{}/Pipeline/__init__.py".format(project_name),
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"

]

for filename in directories_list:
    filepath=Path(filename)
    fildir,file=os.path.split(filepath)

    if fildir!="":
        os.makedirs(fildir,exist_ok=True)
        logging.info("The directory {} is created".format(fildir))

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):

        with open(filepath,'w') as f:
            pass
            logging.info("The directory {} and file is created {}".format(fildir,file))
    else:
        logging.info("The file {}  is existing ".format(file))
