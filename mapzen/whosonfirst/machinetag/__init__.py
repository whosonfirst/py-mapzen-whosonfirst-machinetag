# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import re
import machinetag as mt

class sanitize(mt.sanitize):

    def prepare (self, before):
        after = before

        after = after.replace("&", " and ")	
        after = after.replace("/", " or ")

        after = re.sub(r'\s+', ' ', after)
        after = after.replace(" ", "_")

        after = after.lower()
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

        self.__enpathify_separator__ = "/"

    # https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-pathhierarchy-tokenizer.html
    # https://stackoverflow.com/questions/24819234/elasticsearch-using-the-path-hierarchy-tokenizer-to-access-different-level-of

    def enpathify(self):
        sep = self.__enpathify_separator__
        return sep.join((self.namespace(), self.predicate(), self.value()))
