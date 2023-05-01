import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def to_acronym(string):
    words = string.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym