import subprocess
from nbconvert import PythonExporter
import nbformat
import sys

def execute_notebook(notebook_path):
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = f.read()

    # Convert the notebook to a Python script
    nb = nbformat.reads(notebook_content, as_version=4)
    exporter = PythonExporter()
    py_script, _ = exporter.from_notebook_node(nb)

    # Save the Python script to a temporary file
    tmp_script_path = "tmp_script.py"
    with open(tmp_script_path, 'w', encoding='utf-8') as f:
        f.write(py_script)

    # Execute the Python script within a subprocess
    subprocess.run(["python", tmp_script_path])

if __name__ == "__main__":
    
    parameter_value='comprint/data/examples_input/facehub-fake.png'
    #execute_notebook(notebook_path)
    script_path1 = "ante_detection.py"
    subprocess.run(["python", script_path1,parameter_value])
    script_path2 = "my_run_forgery.py"
    subprocess.run(["python", script_path2,parameter_value])
