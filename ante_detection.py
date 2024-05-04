from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import sys


def show_image(image_path, plot, figsize=(8,8)):
    if plot:
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

def ante_fusion(plot_figs=False):
    output_folder = "./out2"
    input_image_path = sys.argv[1]
    show_image(input_image_path,plot=plot_figs)
    import forgery_detection
    output_image_path_adq1 = create_output_image_path(input_image_path, output_folder, "ADQ1")
    forgery_detection.adq1(input_image_path, output_image_path_adq1)
    show_image(output_image_path_adq1,plot=plot_figs)
    output_image_path_blk = create_output_image_path(input_image_path, output_folder, "BLK")
    forgery_detection.blk(input_image_path, output_image_path_blk)
    show_image(output_image_path_blk,plot=plot_figs)
    output_image_path_dct = create_output_image_path(input_image_path, output_folder, "DCT")
    forgery_detection.dct(input_image_path, output_image_path_dct)
    show_image(output_image_path_dct,plot=plot_figs)
    output_image_path_cagi = create_output_image_path(input_image_path, output_folder, "CAGI")
    forgery_detection.cagi(input_image_path, output_image_path_cagi)
    show_image(output_image_path_cagi,plot=plot_figs)
    # Requires Tensorflow & Comprint repository
    import forgery_detection_comprint_noiseprint
    output_file_heatmap_path_noiseprint = create_output_image_path(input_image_path, output_folder, "Noiseprint", output_type="heatmap")
    output_file_fingerprint_path_noiseprint = create_output_image_path(input_image_path, output_folder, "Noiseprint", output_type="fingerprint")
    noiseprint_model_path = "./comprint/models/noiseprint_nets/net"
    forgery_detection_comprint_noiseprint.noiseprint(input_image_path, output_file_fingerprint_path_noiseprint, output_file_heatmap_path_noiseprint, noiseprint_model_path)    
    show_image(output_file_fingerprint_path_noiseprint,plot=plot_figs)
    show_image(output_file_heatmap_path_noiseprint,plot=plot_figs)
    output_file_heatmap_path_comprint = create_output_image_path(input_image_path, output_folder, "Comprint", output_type="heatmap")
    output_file_fingerprint_path_comprint = create_output_image_path(input_image_path, output_folder, "Comprint", output_type="fingerprint")    
    comprint_model_path = "./comprint/models/Comprint_Siamese_Full_jpg_ps_full/"
    forgery_detection_comprint_noiseprint.comprint(input_image_path, output_file_fingerprint_path_comprint, output_file_heatmap_path_comprint, comprint_model_path)
    show_image(output_file_fingerprint_path_comprint,plot=plot_figs)
    show_image(output_file_heatmap_path_comprint,plot=plot_figs)
    output_file_heatmap_path_comprint_plus_noisprint = create_output_image_path(input_image_path, output_folder, "Comprint+Noiseprint", output_type="heatmap")
    forgery_detection_comprint_noiseprint.comprint_plus_noiseprint(input_image_path, output_file_fingerprint_path_comprint, output_file_fingerprint_path_noiseprint, output_file_heatmap_path_comprint_plus_noisprint)
    show_image(output_file_heatmap_path_comprint_plus_noisprint,plot=plot_figs)
    # Requires torch & CAT-Net repository
    # Also run ./download_weights from the ./CAT-Net repository
    import forgery_detection_catnet
    output_file_heatmap_path_catnet = create_output_image_path(input_image_path, output_folder, "CATNet")
    catnet_modelpath = "./CAT-Net/output/splicing_dataset/CAT_full/CAT_full_v2.pth.tar"
    forgery_detection_catnet.catnet(input_image_path, output_file_heatmap_path_catnet, catnet_modelpath,use_gpu=False)
    show_image(output_file_heatmap_path_catnet,plot=plot_figs)
    
    
    
ante_fusion()