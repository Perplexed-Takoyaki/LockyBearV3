
"""other possibility =

def encrypt():
    return(data[::-1])

new_password = encrypt()
print(new_password)"""



def encrypt(data) :
    num = len(data) - 1
    mod_data = ""
    while num >= 0 :
        mod_data = mod_data + data[num]
        num = num - 1
    return "$$" + mod_data + "$$"


def decrypt(data) :
    dec_data = ""
    if data.startswith("$$") and data.endswith("$$"):
        trim_data = data[2:-2]
    num = len(trim_data) - 1
    while num >= 0 :
        dec_data = dec_data + trim_data[num]
        num = num - 1
    return dec_data