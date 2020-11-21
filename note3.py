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

msg = 'Hello world'
print(message2bin(msg))
print(len(message2bin(msg)))
encoding = 'utf-8'
# bin2message(message2bin(msg))
# print(bytearray(message2bin(msg), 'utf-8').decode(encoding))
# print(bin(76))
print(b'1010111011'.decode(encoding)) #{message2bin(msg)}
print(b'1010111011')

str2 = bytes("hello world", encoding="UTF-8")
print(str2)
print(type(str2))

def char_generator(message):
  for c in message:
    yield ord(c)

msg = 'Hello world'
print(char_generator(msg))
print(ord('e'))
# print(ord(b'01001000'))
# print(chr(1001000))

msg_bin = message2bin(msg)
print(msg_bin[:7])
pos = np.array([64,32,16,8,4,2,1])
print(pos)
 # np.dot( msg_bin[:7], pos)
ls1 = ['1','1','0','0','1','0','1']
ls1 = list(map(int, ls1))
print(ls1)
ls1 = np.array(ls1)
res = ls1.dot(pos)
print(res)


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

ls_tmp = list(['1', '0', '0', '1', '0', '0'])
print('Type ls_tmp is {} =========='.format(type(ls_tmp)))
ls_tmp.append('0')
print('res1 is {}'.format(ls_tmp))

val = int_content_of_byte(['1','1','0','0','1','0','1'])
print('val is {}'.format(val))

msg_list = ['1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0']
msg_list = ['1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0']
print(len(msg_list))

print('Ord of space is {}'.format(ord(' ')))
buffer = []
print('d is {}'.format(ord('d')))
for i in range(0, len(msg_list), 7):
    print(msg_list[i:7+i])
    if (i+7 <= len(msg_list)):
        print(int_content_of_byte(msg_list[i:7+i]))
        print(chr(int_content_of_byte(msg_list[i:7+i])))
    else:
        ls_tmp = list(msg_list[i:])
        zeros_to_pad = 7 - len(msg_list[i:])
        print('Zeros to pad is {}'.format(zeros_to_pad))
        for i in range(zeros_to_pad):
            ls_tmp.append('0')
        # ls_tmp2 = np.pad(ls_tmp, (0, zeros_to_pad), 'constant')
        print('--------------- ls_tmp is {}'.format(ls_tmp))
        print(int_content_of_byte( ls_tmp ))  # msg_list[i:7 + i].append('0')

