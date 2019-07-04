def convertToHexColor(word):
    """Take any string and covert it to a hex color for use in CSS

    Author: Wayne Simmerson <wsimmerson@gmail.com>

    Parameters:
    argument1 (string): String to be converted

    Returns:
    string: Converted hex color code
    """

    word = "AB" + word.upper()
    buff = ""
    for c in word:
        buff += "{}".format(ord(c))
    word = "000000" + hex(int(buff)).lstrip("0x")

    return "#" + word[-6:]

if __name__ == '__main__':
    print(convertToHexColor("Test Name"))