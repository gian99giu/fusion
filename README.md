Hello,
To make this code works:
First of all, in a linux system, create a virtual enviroment with python 3.9 .
The install requirements in the two txt tiles:

pip install -r requirements_tf.txt
pip install -r requirements_torch_catnet.txt

For any problem i leave a .yml file to clone my enviroment. 

In original files there is a confict: torch 1.1.0 is only available for enviroments with python <= 3.7 and it is a problem.
The part of the code that uses torch is perfectly compatible with torch = 1.7.1 or 1.4.0 (tested). This change is already done in txt files.

The you need to install the pretrained weights of this net, run: bash download_fusion_weights.sh, then you have to download CAT and comprint weights, and put the in the right filesystem.
Then it is possible to execute the code.
There is still a problem in the execution in the .ipynb file .
It gives 2 errors: the first about a difficut to extract some PILLOW libraries, and the other about Symbolic Tensor don't have attribute numpy() . This file shows a bigger problem, it gives always different and wrong outputs (?) .

It is sufficient, to get the output, to run my_fusion.py file, it works actually.

Changes in the code:
Changes done by me are minor, linked to compatibility with more recent version of numpy and to ensure eager execution with tensorflow.
