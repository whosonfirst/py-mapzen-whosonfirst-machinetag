import re
import string
import logging

import machinetag.common as mt

class sanitize(mt.sanitize):

    def prepare (self, before):

        after = before.strip()

        if after == "":
            return ""
            
        after = after.lower()
            
        after = after.replace("&", " and ")	
        after = after.replace("/", " or ")

        try:

            # I hate you, Python...
            # https://stackoverflow.com/questions/11692199/string-translate-with-unicode-data-in-python
            # after = string.translate(after, None, string.punctuation)

            after = after.encode('utf-8').translate(None, string.punctuation)

            # the py-3 version... https://stackoverflow.com/questions/23175809/typeerror-translate-takes-one-argument-2-given-python
            # after = after.translate(str.maketrans('','',string.punctuation))

        except Exception, e:
            logging.warning("failed to translate '%s' because %s" % (after, e))
            pass

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
    # https://github.com/whosonfirst/es-whosonfirst-schema/blob/categories/schema/mappings.spelunker.json

    def enpathify(self):
        sep = self.__enpathify_separator__
        return sep.join((self.namespace(), self.predicate(), self.value()))
