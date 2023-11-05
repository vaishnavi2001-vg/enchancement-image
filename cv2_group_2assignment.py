import streamlit as st
import cv2
import numpy as np

def main():
   # Load an image
   image = cv2.imread('image5.jpeg')

   if image is not None:
    height, width = image.shape[:2]
   else:
    st.error("Failed to load the image or unexpected image shape.")
    st.stop()  # Stop the script if the image loading fails


    # Define the transformation matrix for different affine transformations
# 1. Translation
    translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])  # Translate 50 pixels right and 30 pixels down

# 2. Rotation
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)  # Rotate by 45 degrees

# 3. Scaling
    scaling_matrix = np.float32([[0.5, 0, 0], [0, 2, 0]])  # Scale by 50% horizontally and 200% vertically

# 4. Shearing
    shearing_matrix = np.float32([[1, 0.2, 0], [0.2, 1, 0]])  # Shear horizontally by 20% and vertically by 20%

    
    # Apply the affine transformations
    translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    scaled_image = cv2.warpAffine(image, scaling_matrix, (width, height))
    sheared_image = cv2.warpAffine(image, shearing_matrix, (width, height))

    # Display the transformed images
    st.image(image, caption='Original Image', use_column_width=True)
    st.image(translated_image, caption='Translated Image', use_column_width=True)
    st.image(rotated_image, caption='Rotated Image', use_column_width=True)
    st.image(scaled_image, caption='Scaled Image', use_column_width=True)
    st.image(sheared_image, caption='Sheared Image', use_column_width=True)

    # Load a grayscale image and apply contrast enhancement
    enhanced_image = cv2.equalizeHist(image)
    st.image(enhanced_image, caption='Contrast Enhancement (Histogram Equalization)', use_column_width=True)

    # Apply brightness and contrast adjustment
    alpha = 1.5  # Contrast control (1.0 means no change)
    beta = 30    # Brightness control (0 means no change)
    enhanced_image1 = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    st.image(enhanced_image1, caption='Brightness and Contrast Adjustment', use_column_width=True)

    # Apply Gaussian blur
    image2 = cv2.GaussianBlur(image, (5, 5), 0)
    st.image(image2, caption='Smoothing and Blurring (Gaussian Blur)', use_column_width=True)

    # Apply sharpening
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    st.image(sharpened_image, caption='Sharpening (Unsharp Masking)', use_column_width=True)

    # Apply color balance adjustment
    corrected_image = cv2.xphoto.createSimpleWB()
    corrected_image = corrected_image.balanceWhite(image)
    st.image(corrected_image, caption='Color Balance Adjustment', use_column_width=True)

if __name__ == '__main__':
    main()
