import subprocess
from nbconvert import PythonExporter
import nbformat
import sys
import os
from glob import glob

def filter_images(directory):
    filtered_images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith("orig.jpg") and not file.endswith("mask.png"):
                filtered_images.append(os.path.join(root, file))
    return filtered_images

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

if __name__ == "__main__":
    #dataset_dir="C:\Users\Sangi\Documents\dataset\IMD2020"
    dataset_dir='IMD2020'
    image_list = filter_images(dataset_dir)
    for image in image_list:
        parameter_value=image
        print('-------\n',image,'\n----------')
        param2="./results imd2020"
        create_folder_if_not_exists(param2)
        script_path1 = "ante_detection.py"
        subprocess.run(["python", script_path1,parameter_value,param2,'False'])
        script_path2 = "my_run_forgery.py"
        subprocess.run(["python", script_path2,parameter_value,param2,'False'])
        
        
        
        
    

    image_list2 = glob('label_in_wild/images/*')

    for i in image_list2:
        parameter_value2=i
        print('-------\n',i,'\n----------')
        param3="./results in the wild"
        create_folder_if_not_exists(param3)

        script_path3 = "ante_detection.py"
        subprocess.run(["python", script_path3,parameter_value2,param3,'False'])
        script_path4 = "my_run_forgery.py"
        subprocess.run(["python", script_path4,parameter_value2,param3,'False'])
    

    

 