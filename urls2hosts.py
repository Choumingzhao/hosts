# -*- encoding: utf-8 -*-
import sys

def url_to_hosts(f_path):
    with open(f_path) as f:
        for line in f:
            if line.startswith('#') or line.strip() == '':
                print(line, end='')
            else:
                print("0.0.0.0 " + line, end='')

if __name__ == "__main__":
    f_path = sys.argv[-1]
    url_to_hosts(f_path)