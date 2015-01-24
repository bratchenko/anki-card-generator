# -*- coding: utf-8 -*-
import datetime
import os
import sys
import re
import csv

"""hack in local sources if requested and handle import crash"""
if '--local' in sys.argv:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src')) 
try:
    from pystardict import Dictionary
except ImportError, e:
    if __name__ == '__main__':
        print Exception('No pystardict in PYTHONPATH. Try --local parameter.')
        exit(1)
    else:
        raise e

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def demo():
    
    words = open('words.txt', 'r');
    dicts_dir = os.path.join(os.path.dirname(__file__))
    dict = Dictionary(os.path.join(dicts_dir, 'LingvoUniversalEnRu'))
    writer = csv.writer(open('result.tsv', 'wb'), delimiter='	');        

    for w in words:
        w = w.rstrip()
        if dict.get(w):
            print w;
            translation = remove_html_tags(dict.dict[w]).replace("\n", "<br>");
            writer.writerow([w, translation])

if __name__ == '__main__':
    demo()
