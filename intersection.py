import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def iou(img_path, grnd_path, plot=True):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    grnd = cv2.imread(grnd_path, cv2.IMREAD_GRAYSCALE)

    # Resize
    if img.shape > grnd.shape:
        img = cv2.resize(img, (grnd.shape[1], grnd.shape[0]))
    else:
        grnd = cv2.resize(grnd, (img.shape[1], img.shape[0]))

    # Otsu 
    _, img_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # intersection o
    intersection = cv2.bitwise_and(img_thresh, grnd)

    area_intersection = np.sum(intersection > 0)
    area_img = np.sum(img_thresh > 0)
    area_grnd = np.sum(grnd > 0)
    area_union = area_img + area_grnd - area_intersection

    # Calculate Intersection over Union (IoU)
    iou_value = area_intersection / area_union

    if plot:
        fig, axs = plt.subplots(2, 3, figsize=(15, 10))

        axs[0, 0].imshow(img, cmap='gray')
        axs[0, 0].set_title('Image')
        axs[0, 0].axis('off')

        axs[0, 1].imshow(grnd, cmap='gray')
        axs[0, 1].set_title('Ground Truth')
        axs[0, 1].axis('off')

        axs[1, 0].imshow(img_thresh, cmap='gray')
        axs[1, 0].set_title('Image Threshold (Otsu)')
        axs[1, 0].axis('off')

        axs[0, 2].imshow(intersection, cmap='gray')
        axs[0, 2].set_title('Intersection')
        axs[0, 2].axis('off')

        axs[1, 2].axis('off')

        plt.tight_layout()
        plt.show()

        print("Intersection over Union (IoU):", iou_value)

    intersection_folder = 'intersection'
    if not os.path.exists(intersection_folder):
        os.makedirs(intersection_folder)

    
    intersection_filename = os.path.splitext(os.path.basename(img_path))[0] + "_intersection "+ str(iou_value )+".png"
    intersection_path = os.path.join(intersection_folder, intersection_filename)
    cv2.imwrite(intersection_path, intersection)#save the file created

    return intersection, iou_value







    

def calculate_iou_for_folder(ground_truth_path,  img_folder_path, kernel=np.ones((15, 15), np.uint8), plot=True):

    img_prefix = ground_truth_path[11:-9]#get the name of the image
    
    img_files = [f for f in os.listdir(img_folder_path) if f.startswith(img_prefix) and not f.endswith(".npz")]
    # Iterate over the corresponding images
    for img_file in img_files:
        img_path = os.path.join(img_folder_path, img_file)
            
        print(f"Calculating IoU for {img_file} and {img_prefix}...")
        intersection ,intersection_values = iou(img_path, ground_truth_path)
        print("="*50)


# Example usage
ground_truth_path = 'IMD2020/z2/00006_fake_mask.png'
img_folder_path = 'results imd2020'
calculate_iou_for_folder(ground_truth_path,  img_folder_path)
