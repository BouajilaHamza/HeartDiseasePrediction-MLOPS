import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlProject"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/__init__.py",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/components/__init__.py",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/utils/__init__.py",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/utils/common.py",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/config/__init__.py",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/config/configuration.py",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/pipeline/__init__.py",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/entity/__init__.py",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/entity/config_entity.py",
    f"C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"


]




for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")