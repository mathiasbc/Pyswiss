# -*- coding: utf-8 -*-
import sys, traceback

'''
the function print_exc_plus() returns a more detailed traceback when handling
exceptions, it uses the property or linked list between frame nodes
'''

def print_exc_plus():
    '''Detailed version of traceback.print_exc()'''
    tb = sys.exc_info()[2]
    while tb.tb_next:
        tb = tb.tb_next()
    stack = []
    f = tb.tb_frame
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse()
    traceback.print_exc()
    print "Locals by frame, innermost last"
    for frame in stack:
        print
        print "Frame %s in %s at line %s" % (
            frame.f_code.co_name,
            frame.f_code.co_filename,
            frame.f_lineno
        )
        for key, value in frame.f_locals.items():
            print "\t%20s = " % key,
            try:
                print value
            except:
                print "<Error while printing value>"
