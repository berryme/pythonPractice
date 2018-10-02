import difflib
import glob

import lxml.etree as ET


def load_files(source_dir, mask):
    dir = str(source_dir + '/' + mask)
    if mask == '*' or mask == '*.*':
        raise Exception("file Mask can not be just a wildcard")
    fileList = glob.glob(str(dir))
    return fileList


def diff_output(source, compared):
    source = source.splitlines(1)
    compared = compared.splitlines(1)
    diff = difflib.unified_diff(source, compared)
    return str(''.join(diff))


def transform(filename):
    dom = ET.parse(filename)
    xslt = ET.parse('StripNil30.xsl')
    transform = ET.XSLT(xslt)
    newdom = transform(dom)

    sourceStr = ET.tostring(dom, pretty_print=True, method="xml", encoding="unicode")
    newStr = ET.tostring(newdom, pretty_print=True, method="xml", encoding="unicode")

    # print(diff_output(sourceStr, newStr))
    diff = diff_output(sourceStr, newStr)
    diff_filename = filename + ".diff"
    difffile = open(diff_filename, "w", encoding="utf-8")
    difffile.write(diff)

    newfilename = filename + ".new"
    stripFile = open(newfilename, "w", encoding="utf-8")
    stripFile.write(str(newStr))


if __name__ == '__main__':
        transform()

