import os, sys
from pathlib import Path
import logging

while True:
    project_neme = input("Enter your Project Name:")

    if project_neme != "":
        break

#src/__init__.py
list_of_files=[
f"{project_neme}/__init__.py",
f"{project_neme}/components/__init__.py",
f"{project_neme}/config/__init__.py",
f"{project_neme}/constants/__init__.py",
f"{project_neme}/entity/__init__.py",
f"{project_neme}/exception/__init__.py",
f"{project_neme}/logger/__init__.py",
f"{project_neme}/pipeline/__init__.py",
f"{project_neme}/utils/__init__.py",
f"config/config.yaml",
"schema.yaml",
"app.py",
"main.py",
"logs.py",
"exception.py",
"setup.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename =os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    
    else:
        logging.info(f"The file path is present at: {filepath}")
