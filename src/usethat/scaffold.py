from importlib import resources
from pathlib import Path
import shutil

def scaffold(path: str="./skeleton", *args, **kwargs):
    """
    Scaffold a minimal python package

    Copy the entire 'skeleton' folder from the package to `destination`.
    """
    destination_path = Path(path)

    if destination_path.exists():
        raise FileExistsError(f"Destination '{path}' already exists")

    data_source = resources.files("usethat").joinpath("skeleton")
    shutil.copytree(data_source, destination_path, *args, **kwargs)
