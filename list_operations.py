


def reverse_string(string):
    # a[start:end]  items start through end-1
    #a[start:]     items start through the rest of the array
    #a[:end]     items from the beginning through end-1
    #a[:]         a copy of the whole array

   #a[start:end:step] # start through not past end, by step

    return string[::-1]

def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]