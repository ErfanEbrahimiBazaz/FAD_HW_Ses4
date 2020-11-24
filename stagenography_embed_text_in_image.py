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


def int_content_of_byte_for_two_bytes(input_byte):
    """
    Calculates the int value of an input 7-bit stream of 0 and 1
    :param input_byte: input 7-bit stream
    :return: int value
    """
    pos = np.array([8192,4096,2048,1024,512,256,128,64, 32, 16, 8, 4, 2, 1])
    ls1 = list(map(int, input_byte))
    ls1 = np.array(ls1)
    res = ls1.dot(pos)
    return res


def int_content_of_byte(input_byte):
    """
    Calculates the int value of an input 7-bit stream of 0 and 1
    :param input_byte: input 7-bit stream
    :return: int value
    """
    pos = np.array([64, 32, 16, 8, 4, 2, 1])
    ls1 = list(map(int, input_byte))
    ls1 = np.array(ls1)
    res = ls1.dot(pos)
    return res


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
            img_cp.append(bin(int(input_array[x, y]))[2:])

    # reshaping the list to match the image size and order
    new_img_arr = np.reshape(img_cp, (input_array.shape[0], input_array.shape[1]))
    return new_img_arr


def convert_image_bin2int(numpy_array):
    """
    Gets a 2D numpy array and converts every cell from string (binary equivelant of a 0 - 255 integer value) to int.
    :param numpy_array: input 2D numpy array with binary values(an image)
    :return: a 2D int numpy array
    """
    # converting the string back to integer
    for i in range(0, numpy_array.shape[0]):
        for j in range(0, numpy_array.shape[1]):
            # print(int(new_img_arr[i, j], 2))
            # print(new_img_arr[i, j])
            numpy_array[i, j] = int(numpy_array[i, j], 2)

    return numpy_array


# This method needs to be completed
# second solution is to insert binary text size to the beginning of the binary message string
def embed_text_in_image(binary_text, input_array):
    """
    Gets a text, takes its binary value, calculates ite length and put its length in the first two bytes of the image.
    :param binary_text: binary text to be embedded at the least significant bit of every pixel.
    :param input_array: a 2D numpy array with int values. Basically a gray scale image.
    :return: void method, embeds message in lsb of the input image (input_array)
    """
    # calculates the binary content of image
    img_array = image_binary_content(input_array)
    flat_img = img_array.flatten()

    # embedding data in the image
    # change it not to start from first two bytes, reserve the first two bytes for message length
    for i in range(len(binary_text)):
        flat_img[i] = flat_img[i][:-1] + str(binary_text[i])

    new_img_array = flat_img.reshape(input_array.shape)

    for i in range(0, new_img_array.shape[0]):
        for j in range(0, new_img_array.shape[1]):
            new_img_array[i, j] = int(new_img_array[i, j], 2)
    return new_img_array


def msgencoder(msg):
    return format(int(bytes(msg, 'utf-8').hex(), base=16), 'b')

def msgdecoder(msg):
    return bytes.fromhex(format(int(msg, base=2), 'x')).decode('utf-8')


def embed_encoded_msg_in_image(img_path, msg_to_encode):
    """
    Takes the path to an image, and encode the input message inside the lsb of the iamge
    :param img_path: path to image to encode message
    :param msg_to_encode: message is str format to encode inside image
    :return: returns the image with encoded message
    """
    img_path = img_path
    # binary content in str format with all lsb = 0
    new_img_arr = image_binary_content_zero_lowest_bit(img_path)
    img = cv.imread(img_path, 1)

    # Maximum binary message size to save is 16383 as only two bytes are reserved for message length.
    msg = msg_to_encode
    print('Message to embed is "{}"'.format(msg))
    msg2bin = msgencoder(msg)
    print('Encoded message length is {}'.format(len(msg2bin)))
    print('Binary content of message is {}'.format(msg2bin))

    # embed the message size in the first two bytes of the message, 14 bytes of the image (14 first lsb)
    # This will later be used to determine the number of pixels to scan
    bin_len = bin(len(msg2bin))
    print('binary lenght of message is {}'.format(bin_len))

    # pad enough zeros to occupy the first two constructed bytes
    # 14 first lowest significant bits of the image are assigned to the size of the embedded message.
    # Later in reconstructing the message this value will be read to know how many bytes need to be scanned to construct
    # the message.
    # len(bin(len(msg2bin))[2:] shows bit length of the encoded message without the first '0b' at the beginning. That's the
    # reason for 14 and not 16.
    zeros_to_pad = 14 - len(bin(len(msg2bin))[2:])
    length_bytes = '0'
    elm = bin(len(msg2bin))[2:]
    for b in range(zeros_to_pad):
        elm = '0' + elm

    new_msg_to_embed = elm + msg2bin
    print('Message to embed, after adding the zero-padded length to the first of the binary message {}'.format(
        new_msg_to_embed))

    # print(new_img_arr.flatten()) # shape (102400,)
    flat_img = new_img_arr.flatten()

    msg2bin = new_msg_to_embed
    # embedding data in the image
    for i in range(len(msg2bin)):
        flat_img[i] = flat_img[i][:-1] + str(msg2bin[i])

    # reshape flat image to original image size
    new_img_arr2 = flat_img.reshape(new_img_arr.shape)
    for i in range(0, new_img_arr2.shape[0]):
        for j in range(0, new_img_arr2.shape[1]):
            new_img_arr2[i, j] = int(new_img_arr2[i, j], 2)

    # cv2 expects int (MAT)
    # showing the image with embedded data
    # cv.imshow('modified image', new_img_arr2.astype('uint8'))
    return new_img_arr2.astype('uint8')


def decode_message_from_image(img):
    """
    Extracts encoded message from image and decodes it
    :param img: input image with message encoded
    :return: extracted decoded message
    """
    # Reading embedded message from image and decode it
    flat_img_msg = image_binary_content(img).flatten()
    msg_length = []
    for i in range(14):
        msg_length.append(flat_img_msg[i][-1])

    print('======{}'.format(msg_length))

    num_bits_to_scan = int_content_of_byte_for_two_bytes(msg_length)
    print('Number of bits to scan is {}'.format(int_content_of_byte_for_two_bytes(msg_length)))
    num_bits_to_scan += 14

    flat_content = flat_img_msg
    constructed_message = []
    msg_str = ''
    for i in range(num_bits_to_scan):
        constructed_message.append(flat_content[i][-1])
        msg_str += flat_content[i][-1]
    return msgdecoder(msg_str[14:])




img_path = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_Ses4\class\2.jpeg'
msg_to_encode = 'Hello Fenchieeeeeeeeeee jerkieeeeee ßÄÜÖ_!'
img_with_message_encoded = embed_encoded_msg_in_image(img_path,msg_to_encode)
cv.imshow('image with encoded message', img_with_message_encoded)

# Reading embedded data
decoded_msg = decode_message_from_image(img_with_message_encoded)
print('Decoded message extracted from is {}'.format(decoded_msg))

cv.waitKey(0)

