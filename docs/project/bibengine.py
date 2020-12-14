# -*- coding: utf-8 -*-
# Copyright (c) 2020,
# Silvio Peroni <silvio.peroni@unibo.it>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

# The following importing line is used to include in the definition of this class
# the particular functions implemented by a group. The 'my_test_group' module specified
# here is just a placeholder, since it defines only the signature of the various
# functions but it returns always None.
from my_test_group import *


class BibliometricEngine(object):
    def __init__(self, metadata_file_path):
        self.data = process_citations(citations_file_path)

    def compute_impact_factor(self, dois, year):
        return do_compute_impact_factor(self.data, dois, year)

    def get_co_citations(self, doi1, doi2):
        return do_get_co_citations(self.data, doi1, doi2)

    def get_bibliographic_coupling(self, doi1, doi2):
        return do_get_bibliographic_coupling(self.data, doi1, doi2)

    def get_citation_network(self, start, end):
        return do_get_citation_network(self.data, start, end)
    
    def merge_graphs(self, g1, g2):
        return do_merge_graphs(self.data, g1, g2)

    def search_by_prefix(self, prefix, is_citing, dump):
        if dump is None:
            return do_search_by_prefix(self.data, prefix, is_citing)
        else:
            return do_search_by_prefix(dump, prefix, is_citing)

    def search(self, query, field, dump):
        if dump is None:
            return do_search(self.data, query, field)
        else:
            return do_search(dump, query, field)
    
    def filter_by_value(self, query, field, dump):
        if dump is None:
            return do_filter_by_value(self.data, query, field)
        else:
            return do_filter_by_value(dump, query, field)
        
