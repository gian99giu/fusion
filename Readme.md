Hello,
To make this code works:
First of all, in a linux system, create a virtual enviroment with python 3.9 .
Then install requirements:

pip install -r requirements.txt

For any problem i leave a .yml file to clone my enviroment. 

In original files there is a confict: torch 1.1.0 is only available for enviroments with python <= 3.7 and it is a problem.
The part of the code that uses torch is perfectly compatible with torch = 1.7.1 or 1.4.0 (tested). This change is already done in txt files.

You have to download comprint net from github.
Be very careful with CAT-NET installation, just take the weights, or the minimum i file you need that i didn't uploaded.
The you need to install the pretrained weights of this net, run: bash download_fusion_weights.sh, then you have to download CAT and comprint weights, and put the in the right filesystem.
Then it is possible to execute the code.
There is still a problem in the execution in the .ipynb file .

It is sufficient, to get the final output:
1) run the run_forgery_detection_fusion useful.ipynb file, so you can get the result of ADQ1, comprint etc...
2) run my_fusion.py, to get the fusion

About Intersectuion:
The code creates IoU for all images in a folder called 'IMDV2', it's simply a random subset of IMD2020 dataset. The results of fusion for IMD2020 dataset should be in 'results imd2020' folder, change these directories accordingly with your modifications. 

About Oracle:
First you need the folder of intersection created above. 
The oracle consider all the images of IoU produces 2 images:
  The first one consider all the pixel, in common with the ground truth, that were been detected, by all methods, as an artifact.
  The second one considers all the pixel, not in common with the ground, that have been detected, by all metods as an arrtifact.
