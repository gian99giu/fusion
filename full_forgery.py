import subprocess
from nbconvert import PythonExporter
import nbformat
import sys

if __name__ == "__main__":
    
    parameter_value='comprint/data/examples_input/facehub-fake.png'
    script_path1 = "ante_detection.py"
    subprocess.run(["python", script_path1,parameter_value])
    script_path2 = "my_run_forgery.py"
    subprocess.run(["python", script_path2,parameter_value])
