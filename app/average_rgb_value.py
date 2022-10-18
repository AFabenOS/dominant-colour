import os
from PIL import Image
import numpy as np
import cv2

m_img = cv2.imread('100.png')
avg_colour_row = np.average(m_img)
avg_colour = np.average(avg_colour_row)
print(avg_colour)

# class RGBGetter:
#     def __init__(self):
#         pass
    
#     def get_image_location(self):
#         """Retrieves the filename needed for analysis"""
#         # Get the filename
#         # THIS NEEDS TO BE ABLE TO ITERATE THROUGH EVERY FILE

#         frame_directory = r'video_frames/'
#         file_name = os.path.join(frame_directory, '256.png')
#         return file_name

#     def convert_image_rgb(self, file_name):
#         img = Image.open(file_name)
#         # Convert the image to rgb
#         img = img.convert('RGB')
#         return img

#     def get_width_and_height(self, img):
#         width, height = img.size
#         return width, height

#     def get_most_common_colour_values(self, width, height):
#         # Initialise three variables to store 
#         r_total = 0
#         g_total = 0
#         b_total = 0

#         count = 0

#         for x in range(0, width):
#             for y in range(0, height):
#                 r, g, b = img.getpixel((x, y))
#                 r_total += r
#                 g_total += g
#                 b_total += b
#                 count += 1
#         return r_total, g_total, b_total, count

#     def retrieve_rgb_values(self, r_total, g_total, b_total, count):
#         most_common_colour = []

#         r_value = r_total/count
#         g_value = g_total/count
#         b_value = b_total/count

#         most_common_colour.append(r_value)
#         most_common_colour.append(g_value)
#         most_common_colour.append(b_value)

#         return most_common_colour

#     def most_common_rgb_values(self):
#         img_loc = self.get_image_location()
#         rgb_convert = self.convert_image_rgb(img_loc)
#         image_dimensions = self.get_width_and_height(rgb_convert)
#         most_common_rgb_values = self.get_most_common_colour_values(rgb_convert, image_dimensions)
#         rgb_values = self.retrieve_rgb_values(most_common_rgb_values)
#         print(rgb_values)
#         return rgb_values

# test_class = RGBGetter()
# test_class.most_common_rgb_values()



# # Loop over the frames
# for file in os.listdir(frame_directory):
#     f_name = os.fsdecode(file)
#     if f_name.endswith(".png"):
#         print(os.path.join(frame_directory, f_name))

#     else:
#         continue

# Next need to get most dominant colour through cv2, pillow or numpy