# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import re
import machinetag as mt

class sanitize(mt.sanitize):

    def prepare (self, before):
        after = before
        after = after.replace("&", "and")
        after = after.replace(" ", "_")
        after = after.lower()

        # print "%s -> %s" % (before, after)
        return after

    def prepare_namespace(self, ns):
        return self.prepare(ns)

    def prepare_predicate(self, pred):
        return self.prepare(pred)
    
    def prepare_value(value):
        return self.prepare(value)

class machinetag(mt.machinetag):

    def __init__(self, tag):
        mt.machinetag.__init__(self, tag)
