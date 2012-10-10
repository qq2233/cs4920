#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eb import *
from kenkyusha5_gaiji import *
import string
import re

class Kenkyusha5Dumper(object):
    """Dump Kenkyusha 5th EPWING Dictionary into a file
    Sanitises the output for re-importing with Importer"""
    def __init__(self, dictdir):
        super(Kenkyusha5Dumper, self).__init__()
        self.dictdir = dictdir
        eb_initialize_library()
        self.book = EB_Book()
        self.appendix = EB_Appendix() 
        self.hookset = EB_Hookset()
        self.gaiji = KENKYUSHA5_GAIJI

        eb_set_hooks(self.hookset, (
            (EB_HOOK_NARROW_FONT, self.hook_font),
            (EB_HOOK_WIDE_FONT,   self.hook_font),
            (EB_HOOK_BEGIN_REFERENCE, self.hook_begin_reference),
            (EB_HOOK_END_REFERENCE, self.hook_end_reference)))
        try:
            eb_bind(self.book, self.dictdir)
        except EBError, (error, message):
            code = eb_error_string(error)
            sys.stderr.write("Error: %s: %s\n" % (code, message))
            sys.exit(1)
        eb_set_subbook(self.book, 0)

    def hook_font(self, book, appendix, container, code, argv):
        if (code, argv[0]) in self.gaiji:
            replacement = "{{0x{}}}".format(
                    self.gaiji[(code, argv[0])].encode('hex'))
        else:
            replacement = '#'
        eb_write_text_string(book, replacement)
        return EB_SUCCESS

    def hook_begin_reference(self, book, appendix, container, code, argv):
         eb_write_text_string(book, "<LINK>")
         return EB_SUCCESS

    def hook_end_reference(self, book, appendix, container, code, argv):
        eb_write_text_string(book, "</LINK[{:d}:{:d}]>".format(
            argv[1], argv[2]))
        return EB_SUCCESS

    def get_content(self):
        buffer = []
        while 1:
            data = eb_read_text(self.book, self.appendix, 
                    self.hookset, None)
            if not data:
                break
            buffer.append(data)
        data = string.join(buffer, "")
        return data

    def replace_gaiji_hex_sub_helper(self, match):
        """Returns the utf-8 gaiji given the utf-8 hex code
        for the gaiji"""
        return match.group(1).decode('hex')

    def replace_gaiji_hex(self, utf8_string):
        """Given a UTF-8 string, replace all instances of gaiji
        hexadecimal tags to appropriate UTF-8 gaiji. Returns 
        a new string with all gaiji hex tags replace with gaiji"""
        #print re.findall("{0x[0-9a-f]+}", utf8_string)
        return re.sub(r'{0x([0-9a-f]+)}', 
                self.replace_gaiji_hex_sub_helper, utf8_string)

    def dump(self, outfile):
        """Dump to file"""
        #(159979, 1882) is last position with useful info
        #(159979, 1944) is first position with useless info
        #(107887, 872) is the foreword
        #(108260, 1606) is first entry
        fh = open(outfile,"w")
        pos = (108260, 1606)
        eb_seek_text(self.book, pos)
        while pos <= (159979, 1882):
            content = self.get_content()
            utf8_content = content.decode('euc-jp', errors='ignore').encode('utf-8',errors='ignore')
            #print self.replace_gaiji_hex(utf8_content)
            fh.write(self.replace_gaiji_hex(utf8_content))
            pos = eb_tell_text(self.book)
            #print(pos)
            eb_seek_text(self.book, (pos[0], pos[1]+2))
        fh.close()
        
def main():
    dictdir = 'kenkyusha'
    outfile = 'kendump.txt'
    dumper = Kenkyusha5Dumper(dictdir)
    dumper.dump(outfile)

if __name__ == '__main__':
    main()
