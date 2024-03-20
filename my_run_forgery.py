import forgery_detection_fusion_idlab
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os


def show_image(image_path, figsize=(8,8)):
    img_pil = Image.open(image_path)
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(np.array(img_pil).astype(np.uint8))
    ax.grid(False)
    plt.show()

def create_output_image_path(input_image_path, output_folder, method, output_type="heatmap"):
    # Extract the filename from the input image path
    input_image_name = os.path.basename(input_image_path)

    # Construct the output image path
    output_image_name = f"{input_image_name}_{method}_{output_type}.png"
    output_image_path = os.path.join(output_folder, output_image_name)

    return output_image_path
input_image_path = "./examples_input/denise_m23.jpg"
output_folder = "./examples_output"
output_image_path_adq1 = create_output_image_path(input_image_path, output_folder, "ADQ1")
output_image_path_blk = create_output_image_path(input_image_path, output_folder, "BLK")
output_image_path_dct = create_output_image_path(input_image_path, output_folder, "DCT")
output_image_path_cagi = create_output_image_path(input_image_path, output_folder, "CAGI")
output_file_heatmap_path_noiseprint = create_output_image_path(input_image_path, output_folder, "Noiseprint", output_type="heatmap")
output_file_fingerprint_path_noiseprint = create_output_image_path(input_image_path, output_folder, "Noiseprint", output_type="fingerprint")
output_file_heatmap_path_comprint = create_output_image_path(input_image_path, output_folder, "Comprint", output_type="heatmap")
output_file_fingerprint_path_comprint = create_output_image_path(input_image_path, output_folder, "Comprint", output_type="fingerprint")
output_file_heatmap_path_comprint_plus_noisprint = create_output_image_path(input_image_path, output_folder, "Comprint+Noiseprint", output_type="heatmap")
output_file_heatmap_path_catnet = create_output_image_path(input_image_path, output_folder, "CATNet")
catnet_modelpath = "./CAT-Net/output/splicing_dataset/CAT_full/CAT_full_v2.pth.tar"
output_file_heatmap_path_fusion_idlab = create_output_image_path(input_image_path, output_folder, "FusionIDLab")
# This assumes all previous forgery detection methods have been run before, and the corresponding npz files are available
import tensorflow as tf
tf.config.run_functions_eagerly(True)

fusion_idlab_model = "./models/training_checkpoints_faceswap+imd2020+openforensics_balanced_all_methods_just_heatmaps+original_image_l2_batch1_40epochs_v11_only_latest"

forgery_detection_fusion_idlab.run_fusion_idlab(
    input_image_path,
    output_file_heatmap_path_catnet,
    output_file_heatmap_path_comprint_plus_noisprint,
    output_image_path_adq1,
    output_image_path_blk,
    output_image_path_dct,
    output_image_path_cagi,
    output_file_heatmap_path_comprint,
    output_file_heatmap_path_noiseprint,
    output_file_heatmap_path_fusion_idlab,
    fusion_idlab_model, use_gpu=True)
show_image(output_file_heatmap_path_fusion_idlab)