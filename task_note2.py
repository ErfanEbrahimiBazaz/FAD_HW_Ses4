import cv2 as cv
import numpy as np


def message2bin(msg):
    """
    Converts a msg to binary format
    :param msg: message to convert
    :return: binary content of message in string format
    """
    message_bin = ''.join(format(x, 'b') for x in bytearray(msg, 'utf-8'))
    return message_bin


def bin2message(msg_bin):
    """
    Converts a binary content in str format to str message.
    :param msg_bin: binary content of a message in str format: 10101010001111011101101
    :return: string content of message
    """
    pass


def image_binary_content_zero_lowest_bit(img_path):
    """
    gets an image path. Converts the image into grayscale.
    Calculates binary of each image pixel. Makes the lowest value digit to zero.
    To show the returned image makes converstion to uint8
    :param img_path: path to image
    :return: a numpy array of new image content.
    """
    img_path = img_path
    img = cv.imread(img_path, 1)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('original image', img_gray)

    img_cp = []
    for x in range(0, img_gray.shape[0]):
        for y in range(0, img_gray.shape[1]):
            # print(bin(img_gray[x, y])[2:-1] + '1')
            # getting binary content in a string: making last bit zero
            img_cp.append(bin(img_gray[x, y])[2:-1] + '0')

    # reshaping the list to match the image size and order
    new_img_arr = np.reshape(img_cp, (img_gray.shape[0], img_gray.shape[1]))

    # for i in range(0, new_img_arr.shape[0]):
    #     for j in range(0, new_img_arr.shape[1]):
    #         # the last bit is already zero
    #         new_img_arr[i, j] = new_img_arr[i, j]

    # converting the string back to integer
    # for i in range(0, new_img_arr.shape[0]):
    #     for j in range(0, new_img_arr.shape[1]):
    #         # print(int(new_img_arr[i, j], 2))
    #         # print(new_img_arr[i, j])
    #         new_img_arr[i, j] = int(new_img_arr[i, j], 2)

    # cv2 expects int (MAT)
    # cv.imshow('modified image', new_img_arr.astype('uint8'))
    return new_img_arr


def image_binary_content(input_array):
    """
   Calculates the binary content of an input numpy array of type int.
   :param input_array: input numpy array which is a gray_scale image
   :return: binary content of the image in str format
   """

    img_cp = []
    for x in range(0, input_array.shape[0]):
        for y in range(0, input_array.shape[1]):
            # print(bin(img_gray[x, y])[2:-1] + '1')
            print(bin(int(input_array[x, y]))[2:])
            img_cp.append(bin(int(input_array[x, y]))[2:])

    # reshaping the list to match the image size and order
    new_img_arr = np.reshape(img_cp, (input_array.shape[0], input_array.shape[1]))
    return new_img_arr


def convert_image_bin2int(numpy_array):
    """
    Gets a 2D numpy array and converts every cell from string (binary equivelant of a 0 - 255 integer value) to int.
    :param numpy_array: input 2D numpy array (an image)
    :return: a 2D int numpy array
    """
    # converting the string back to integer
    for i in range(0, numpy_array.shape[0]):
        for j in range(0, numpy_array.shape[1]):
            # print(int(new_img_arr[i, j], 2))
            # print(new_img_arr[i, j])
            numpy_array[i, j] = int(numpy_array[i, j], 2)

    return numpy_array


img_path = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_Ses4\class\2.jpeg'
new_img_arr = image_binary_content_zero_lowest_bit(img_path) # binary content in str format
# new_img_arr = convert_image_bin2int(new_img_arr)
img = cv.imread(img_path, 1)

msg= 'Hii darling'
msg2bin = message2bin(msg)
print(len(msg2bin))
print(msg2bin)

# x = new_img_arr.shape[0]
# y = new_img_arr.shape[1]

# # pix = int(len(msg2bin) / y)
# # if (pix != 0):
# #     mod = (pix % x)
# # num_fetched_pixels
print(new_img_arr.flatten()) # shape (102400,)
flat_img = new_img_arr.flatten()

# embeddin data in the image
for i in range(len(msg2bin)):
    print('flat image original value = {}'.format(flat_img[i]))
    print('mesasage binary is {}'.format(msg2bin[i]))
    flat_img[i] = flat_img[i][:-1] + str(msg2bin[i])
    # print('flat image new value = {}'.format(flat_img[i][:-1] + str(msg2bin[i])))
    print('flat image new value = {}'.format(flat_img[i]))
    # flat_img[i] = int(flat_img[i], 2)
    print('new img pixel value is {}'.format(flat_img[i]))

    # print(bin(int(flat_img[i]))[2:-1] + msg2bin[i])
    # flat_img[i] = bin(int(flat_img[i]))[:-1] + msg2bin[i]
    # print('new img pixel value is {}'.format(flat_img[i]))
    print('-----------')

print(new_img_arr.shape)
print(flat_img.shape)
new_img_arr2 = flat_img.reshape(new_img_arr.shape)
print(new_img_arr2.shape)

for i in range(0, new_img_arr2.shape[0]):
    for j in range(0, new_img_arr2.shape[1]):
        new_img_arr2[i, j] = int(new_img_arr2[i, j], 2)
        # print(int(new_img_arr2[i,j], 2))
        # print(new_img_arr2[i,j])

# cv2 expects int (MAT)
# showing the image with embedded data
cv.imshow('modified image', new_img_arr2.astype('uint8'))


# Reading embedded data
num_bits_to_scan = len(msg2bin)
print(type(new_img_arr2))
# for i in range(0, new_img_arr2.shape[0]):
#     for j in range(0, new_img_arr2.shape[1]):
#         print(type(int(new_img_arr2[i, j])))
content_img = image_binary_content(new_img_arr2)
flat_content = content_img.flatten()

constructed_message = []
msg_str=''
for i in range(num_bits_to_scan):
    print('pixel {} with message embedded {}'.format(i, flat_content[i][-1]))
    constructed_message.append(flat_content[i][-1])
    msg_str += flat_content[i][-1]
    # msg_str.join(flat_content[i][-1])

print('constructed message is {}'.format(constructed_message))
print('message string is {}'.format(msg_str))
print(message2bin(msg))
print( bytearray(' ', 'utf-8'))
print(''.join(format(x, 'b') for x in bytearray('H', 'utf-8')))
# print(msg_str.encode('utf8'))
# print('message content: {}'.format( int() ))

#
# #     for x in range(new_img_arr.shape[0]):
# #         for y in range(new_img_arr.shape[1]):
# #             new_img_arr[x,y] = new_img_arr[:-1] + msg2bin[i]



# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('original image', img_gray)
#
# img_cp = []
# for x in range(0, img_gray.shape[0]):
#     for y in range(0, img_gray.shape[1]):
#         # print(bin(img_gray[x, y])[2:-1] + '1')
#         # getting binary content in a string
#         img_cp.append(bin(img_gray[x, y])[2:-1] + '0')
#         # img_cp.append(bin(img_gray[x, y])[2:-1] + '1')
#         # print(bin(img_gray[x, y])[2:-1]+ '0')
#
# # reshaping the list to match the image size and order
# new_img_arr = np.reshape(img_cp, (img_gray.shape[0], img_gray.shape[1]))
#
# # print(new_img_arr.shape)
# # print(type(new_img_arr))
# # print(new_img_arr[-5, -1])
#
# for i in range(0, new_img_arr.shape[0]):
#     for j in range(0, new_img_arr.shape[1]):
#         # making last bit zero
#         new_img_arr[i, j] = new_img_arr[i, j] # [:-1] + '0'
#
#
# # print(new_img_arr.shape)
# # print(new_img_arr[319,319])
# # print(int(new_img_arr[319,319], 2))
#
# # converting the string back to integer
# for i in range(0, new_img_arr.shape[0]):
#     for j in range(0, new_img_arr.shape[1]):
#         print(int(new_img_arr[i,j], 2))
#         print(new_img_arr[i, j])
#         new_img_arr[i, j] = int(new_img_arr[i, j], 2)




# new_img_arr.astype('uint8')
# msg = 'Hii darling'
# print('message length is {}'.format(len(msg)))
# msg_bin = ''.join(format(x, 'b') for x in bytearray(msg, 'utf-8'))
# print(''.join(format(x, 'b') for x in bytearray(msg, 'utf-8')))
# print('Len of byte array is {}'.format( len(''.join(format(x, 'b') for x in bytearray(msg, 'utf-8'))) ))
# msg_len = len(''.join(format(x, 'b') for x in bytearray(msg, 'utf-8')))
# print('Len of byte array is {}'.format( msg_len ))
# print(type(msg_len))
# for i in range(msg_len):
#     print(msg_bin[i])
# print(message2bin(msg))




# print(int('00100001', 2))
# print(len(img_cp))
# print(img_gray.shape[0]* img_gray.shape[1])
# print(bin(225))
# print([' '.join(bytearray(c)) for c in msg])

# cv.imshow('modified image', new_img_arr.astype('uint8'))
cv.waitKey(0)

