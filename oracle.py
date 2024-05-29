import cv2
import numpy as np
import os

def filter_images(directory):
    filtered_images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith("orig.jpg") and not file.endswith("mask.png"):
                filtered_images.append(os.path.join(root, file))
    return filtered_images

def apply_oracle(intersection_folder, ground_truth_path, prefix):
    # Load ground truth image
    ground_truth = cv2.imread(ground_truth_path, cv2.IMREAD_GRAYSCALE)
    if ground_truth is None:
        raise ValueError(f"Ground truth image not found at {ground_truth_path}.")
    height, width = ground_truth.shape

    # Prepare cumulative mask for all intersection images
    cumulative_white = np.zeros((height, width), dtype=np.uint8)

    # Threshold to consider a pixel as white
    white_threshold = 200

    # Process intersection images
    for file_name in os.listdir(intersection_folder):
        file_path = os.path.join(intersection_folder, file_name)
        
        # Load and resize the intersection image
        intersection_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if intersection_image is None:
            continue
        intersection_image_resized = cv2.resize(intersection_image, (width, height))
        
        # Apply threshold to create binary mask for white pixels    
        _, intersection_white = cv2.threshold(intersection_image_resized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)        
        # Update the cumulative white mask using bitwise OR
        cumulative_white = cv2.bitwise_or(cumulative_white, intersection_white)

    # Apply threshold to the ground truth image to create a binary mask
    _, ground_truth_white = cv2.threshold(ground_truth, white_threshold, 255, cv2.THRESH_BINARY)

    # Create output images
    image1 = cv2.bitwise_and(cumulative_white, ground_truth_white)
    image2 = cv2.bitwise_and(cumulative_white, cv2.bitwise_not(ground_truth_white))

    # Save the output images
    cv2.imwrite((str(prefix)+'artifact_in_gound.png'), image1)
    cv2.imwrite((str(prefix)+'artifact_out_ground.png'), image2)

    print("Processing complete.")



intersection_folder = 'inter_oracle'
img_list = filter_images('IMDV2')
i=0
for img_path in img_list:
    img_name = img_path
    ground_path = img_path[:-4] + '_mask.png'
    apply_oracle(intersection_folder,ground_path,i)
    i = i+1


    


    