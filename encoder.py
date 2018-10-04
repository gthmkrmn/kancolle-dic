# -*- coding:utf-8 -*-
import codecs

def main():
    sysin_path  = './equipments.txt'
    sysout_path = './Unicode/equipments.txt'

    sysin  = codecs.open(sysin_path, "r", "utf-8")
    sysout = codecs.open(sysout_path, "w", "utf-16")
    for row in sysin:
        sysout.write(row)
    sysin.close()
    sysout.close()

if __name__ == '__main__':
    main()