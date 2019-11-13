from pathlib import Path
from subprocess import run

input_dir = Path("/home/codyjackson/PycharmProjects/ThePythonGameBook/pygame")
files = [file for file in input_dir.iterdir()]

for file in files:
    try:
        if file.name.endswith(".py"):
            run(["2to3", "-w", "-n", "-j 6", file])
    except Exception as e:
        print(e)
