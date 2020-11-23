import numpy as np
import cv2 as cv
import os


def mask_n_bit_of_image(img_array, mask):
    """
    Applies a mask bitwise on an image to make the n lowest bit zero
    :param img: input image
    :param mask: mask to make the n lowest significant bits zero. Maske sample: int('11111110', 2)
    :return: masked image
    """
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            new_value = img_array[i, j] & mask
            img_array[i, j] = new_value

    return img_array


def draw_img_side_by_side(img1, img2, caption):
    h_im = cv.hconcat([img_cp, img])
    cv.imshow(caption, h_im)


def image_binary_content(input_array):
    """
   Calculates the binary content of an input numpy array of type int.
   :param input_array: input numpy array which is a gray_scale image
   :return: binary content of the image in str format
   """

    img_cp = []
    for x in range(0, input_array.shape[0]):
        for y in range(0, input_array.shape[1]):
            img_cp.append(bin(int(input_array[x, y]))[2:])

    # reshaping the list to match the image size and order
    new_img_arr = np.reshape(img_cp, (input_array.shape[0], input_array.shape[1]))
    return new_img_arr


def padding_zeros_to_make_8bits_images(input_image):
    """
    Checks the output of image_binary_content(img) to add zeros to the left hand side of every byte.
    It makes sure every pixel is represented by 8 bytes
    :param input_image: input image or numpy 2D array
    :return: numpy 2D array of 8-bits pixels in binary format
    """
    for i in range(input_image.shape[0]):
        for j in range(input_image.shape[1]):
            if len(input_image[i, j]) < 8:
                # print(input_image[i, j])
                zeros_to_pad = 8 - len(input_image[i, j])
                # print('Zeros to pad is {}'.format(zeros_to_pad))
                elm = input_image[i, j]
                for b in range(zeros_to_pad):
                    elm = '0' + elm
                # print('New value is {} '.format(elm))
                input_image[i, j] = elm
                # print('double check {} '.format(input_image[i, j]))

    return input_image



def write_img(path, name, img):
    """

    :param path:
    :param name:
    :param img:
    :return:
    """
    name = os.path.join(path, name)
    cv.imwrite(name, img)



img_path = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\Sol_ses3\base.png'
# img_path = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_Ses4\pratices\azara.jpg'

img = cv.imread(img_path, 0)
cv.imshow('original image', img)
img_cp = img.copy()
path_dest = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_Ses4\HW\color'
print('Original image shape {}'.format(img.shape))

'''
mask = int('11111110', 2)
print('mask = {}'.format(mask))
img_n1 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n1, 'Modified image n=1')
write_img(path_dest, 'cn1.jpg', img_n1)


mask = int('11111100', 2)
print('mask = {}'.format(mask))
img_n2 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n2, 'Modified image n=2')
write_img(path_dest, 'cn2.jpg', img_n2)


mask = int('11111000', 2)
print('mask = {}'.format(mask))
img_n3 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n3, 'Modified image n=3')
write_img(path_dest, 'cn3.jpg', img_n3)


mask = int('11110000', 2)
print('mask = {}'.format(mask))
img_n4 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n4, 'Modified image n=4')
write_img(path_dest, 'cn4.jpg', img_n4)


mask = int('11100000', 2)
print('mask = {}'.format(mask))
img_n5 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n5, 'Modified image n=5')
write_img(path_dest, 'cn5.jpg', img_n5)


mask = int('11000000', 2)
print('mask = {}'.format(mask))
img_n6 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n6, 'Modified image n=6')
write_img(path_dest, 'cn6.jpg', img_n6)


mask = int('10000000', 2)
print('mask = {}'.format(mask))
img_n7 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n7, 'Modified image n=7')
write_img(path_dest, 'cn7.jpg', img_n7)


mask = int('00000000', 2)
print('mask = {}'.format(mask))
img_n8 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n8, 'Modified image n=8')
write_img(path_dest, 'cn8.jpg', img_n8)

'''

mask = int('11111100', 2)
print('mask = {}'.format(mask))
img_n2 = mask_n_bit_of_image(img, mask)
# draw_img_side_by_side(img_cp, img_n2, 'Modified image n=2')

img_to_hide_path = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_Ses4\class\2.jpeg'
img_to_hide = cv.imread(img_to_hide_path, 0)

# for images which are bigger than 1/4 of the base image, resize them:
img_to_hide = cv.resize(img_to_hide, (220, 220), interpolation=cv.INTER_NEAREST)


cv.imshow('hidden image', img_to_hide)

h_flat = img_to_hide.flatten()
print('LENGTH OF FLAT HIDDEN IMAGE IS {}'.format(len(h_flat)))
# for i in range(len(h_flat)):
#     print(bin(h_flat[i]))

img_hidden_bin = image_binary_content(img_to_hide)
print('binary of hidden image type: {}'.format(type(img_hidden_bin)))
# reformat evey byte of the hidden image to have 8 bits pixels
img_hidden_bin = padding_zeros_to_make_8bits_images(img_hidden_bin)
print(img_hidden_bin.shape)

all_pixels_hidden_img = img_hidden_bin.flatten()

print('Length of flattened hidden image to embed is {}'.format(len(all_pixels_hidden_img)))
# for i in range(0, 48400):
#     print(all_pixels_hidden_img[i])

num_pixels_to_modify = len(all_pixels_hidden_img) * 4
print('Number of pixels to modify in base image is {}'.format(num_pixels_to_modify))

# parts = [your_string[i:i+n] for i in range(0, len(your_string), n)]
two_bit_message_list = []
for row in all_pixels_hidden_img:
    for i in range(0, 8, 2):
        two_bit_message_list.append(row[i: i+2])
print('TWO BITS MESSAGE LIST LENGTH {}'.format(len(two_bit_message_list)))
# reconstruct the hidden msg to make sure for the next part
# c_h_img = []
# for i in range(0, len(two_bit_message_list), 4):
#     const_byte = two_bit_message_list[i] + two_bit_message_list[i+1] + two_bit_message_list[i+2] + two_bit_message_list[i+3]
#     c_h_img.append(const_byte)
#
# print('constructed image length c_h_img {}'.format(len(c_h_img)))
# for i in range(48400):
#     print(c_h_img[i])
# c_h_img = np.array(c_h_img, np.float64)
# c_h_img = c_h_img.reshape(img_to_hide.shape)
# cv.imshow('C_H_IMG', c_h_img.astype('uint16'))


# insert 6 zeros to left hand side of every entry to two_bit_message_list
new_hidden_image = []
for row in two_bit_message_list:
    row = '000000' + row
    new_hidden_image.append(row)

base_img_flat = img_cp.flatten()
num_bytes_to_fetch = len(two_bit_message_list)
img_base_flat = img_n2.flatten()
print('LENGTH OF TWO BIT MSG LIST {}'.format(num_bytes_to_fetch))

print('Bit length of the bytes to fetch is {} '.format(bin(num_bytes_to_fetch)))
# Reserve the first 3 bytes *(3 * 8 = 24) bytes of the base image) for image size: this is the number of bytes to be
# scanned from new constructed image
print(bin(num_bytes_to_fetch)[2:])
print(len( bin(num_bytes_to_fetch)[2:] ))
# num_reserved_bytes = 20
# zeros_to_pad = num_reserved_bytes - len( bin(num_bytes_to_fetch)[2:] )
# elm = bin(num_bytes_to_fetch)[2:]
# for i in range(zeros_to_pad):
#     elm = '0'+ elm
# print(elm)
# print(len(elm))
#
# two_bit_image_length = []
# for i in range(0, num_reserved_bytes, 2):
#     print(elm[i: i+2])
#     two_bit_image_length.append(elm[i: i+2])


# print('Start of loop to embed binary length of hidden image in the first 10 bytes of the base image')
# for i in range(10):
#     new_value = img_base_flat[i] | int( new_hidden_image[i], 2)
#     img_base_flat[i] = new_value


print('Start of loop to embed the hidden image in base image')
for i in range(num_bytes_to_fetch):
    # First 12 bytes are reserved for the hidden image size to be embedded
    new_value = img_base_flat[i] | int( new_hidden_image[i], 2)
    img_base_flat[i] = new_value

image_with_hidden_img = img_base_flat.reshape(img_n2.shape)
cv.imshow('Image with hidden image embedded', image_with_hidden_img)

# int(img_base_flat[409595])
# print(img_base_flat[409596])
# print(img_base_flat[409597])
# print(img_base_flat[409598])
# print(img_base_flat[409599])




# Reading embedded image from constructed image
# num_bytes_to_fetch
# for i in range(0, image_with_hidden_img.shape[0]):
#     for j in range(0, image_with_hidden_img.shape[1]):
#         print('New image {}'.format(image_with_hidden_img[i, j]))

constructed_image_with_message_embedded = image_binary_content(image_with_hidden_img)
constructed_image_with_message_embedded_zero_padded = padding_zeros_to_make_8bits_images(constructed_image_with_message_embedded)
flat_constructed_image_with_message_embedded = constructed_image_with_message_embedded_zero_padded.flatten()

embedded_img_list = []
for i in range(num_bytes_to_fetch):
#     print(flat_constructed_image_with_message_embedded[i][-2:])
    embedded_img_list.append(flat_constructed_image_with_message_embedded[i][-2:])

# [print(rec) for rec in embedded_img_list]
print('EMBEDDED IMAGE LIST LENGTH {}'.format(len(embedded_img_list)))

const_byte_list = []
for i in range(0, len(embedded_img_list), 4):
    const_byte = embedded_img_list[i] + embedded_img_list[i+1] + embedded_img_list[i+2] + embedded_img_list[i+3]
    const_byte_list.append(const_byte)
    # print(const_byte)

# [print(rec) for rec in const_byte_list]
print('LENGTH OF CONSTRUCT BYTES IS {}'.format(len(const_byte_list)))

const_byte_list_tmp = np.array(const_byte_list, np.float64)
const_byte_2D_array = const_byte_list_tmp.reshape((220,220))
cv.imshow('Constructed image from base', const_byte_2D_array.astype('uint16'))
# h = img_to_hide.flatten()
# for i in range(0, 48400, 4):
#     print(bin(h[i]))

# print('Number of read bytes in the original image {}'.format(len(embedded_img_list)))
#
# num_loop = len(embedded_img_list)//4
# print('Number of loops to reconstruct the bytes {}'.format(num_loop)) ## 48400

# c_h_img = []
# for i in range(0, len(two_bit_message_list), 4):
#     const_byte = two_bit_message_list[i] + two_bit_message_list[i+1] + two_bit_message_list[i+2] + two_bit_message_list[i+3]
#     c_h_img.append(const_byte)

# hidden_img_construct_flat = []
# for i in range(0, num_loop, 4):
#     # new_row = ''
#     # counter = 0
#     new_row = embedded_img_list[i] + embedded_img_list[i+1] + embedded_img_list[i+2] + embedded_img_list[i+3]
#     # print(new_row)
#     hidden_img_construct_flat.append(new_row)
    # for row in embedded_img_list:
    #     new_row = new_row + row
    #     counter += 1
    #     if counter == 4:
    #         print(new_row)
    #         break
#
#     for i in range(4):
#         new_row = new_row + row
#     print(new_row)

# print(img_to_hide.shape)
# print('hidden image construct flat length {}'.format(len(hidden_img_construct_flat)))
# hidden_img_construct_flat = np.array(hidden_img_construct_flat, np.float32)
# constructed_hidden_image = hidden_img_construct_flat.reshape(img_to_hide.shape)

# cv.imshow('Extract embedded image from consructed image', constructed_hidden_image.astype('uint8'))

cv.waitKey(0)
cv.destroyAllWindows()
