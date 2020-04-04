#! /usr/bin/python3

import sys, re
from copy import deepcopy

def isScreenBg(line):
    """
    :param line: a string with some SVG element
    :returns: True if the element is an image which contains the
    screen's background
    """
    if "image" not in line:
        return False
    m=re.match(r'.*width="(\d+)".*', line)
    if m:
        width=int(m.group(1))
        return width > 500
    return False

def dark2light(lines):
    """
    converts the dark style to a light style
    :param lines: a list of strings
    :returns: a list of strings with subsitutions done
    """
    # change some colors and a few widths
    sub = [
        ('fill="#ffff00"', 'fill="#000000"'),
        ('g fill="#008000"', 'g fill="#0000ff"'),
        ('stroke="#22648d"', 'stroke="#ababab"'),
        ('stroke="#00ff00" stroke-opacity="1" stroke-width="1"',
         'stroke="#0000ff" stroke-opacity="1" stroke-width="2"'),
        ('stroke="#ffff00"', 'stroke="#000000"'),
        ('stroke="#ff00ff" stroke-opacity="1" stroke-width="1"',
         'stroke="#00ff00" stroke-opacity="1" stroke-width="2"'),
        ('stroke="#00ffff" stroke-opacity="1" stroke-width="1"',
         'stroke="#00ff00" stroke-opacity="1" stroke-width="2"'),
        ('g fill="none" stroke="#0000ff"', 'g fill="none" stroke="#ff0000"'),
        ('g fill="none" stroke="#ff0000"', 'g fill="none" stroke="#ff00ff"'),
        ('g fill="none" stroke="#000000" stroke-opacity="1" stroke-width="1"',
         'g fill="none" stroke="#000000" stroke-opacity="1" stroke-width="2"'),
    ]
    result=[]
    for l in deepcopy(lines):
        for s in sub:
            l=l.replace(*s)
        if not isScreenBg(l):
            # include all elements but exclude the screen's background image
            result.append(l)
    return result
            
if __name__ == "__main__":
    # from pprint import pprint
    if len(sys.argv) > 2:
        f1 = sys.argv[1]
        f2 = sys.argv[2]
    else:
        f1 = "oscilloscope-screen-dark.svg"
        f2 = "oscilloscope-screen-light.svg"
    f1=open(f1).readlines()
    f2=open(f2).readlines()
    f3=dark2light(f1)
    real_diffs = [ l for l in differences(f3, f2) if re.match(r"^[-\+\?].*", l)]
    for d in real_diffs:
        print(d, end="")
    with open("new.svg","w") as outfile:
        for l in f3:
            outfile.write(l)
