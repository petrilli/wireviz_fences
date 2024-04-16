"""Top-level package for Wireviz Fences."""
from wireviz import wireviz

__author__ = """Christopher Petrilli"""
__email__ = 'petrilli@amber.org'
__version__ = '0.1.0'


def fence_wireviz(source, language, css_class, options, md, classes=None, id_value='',
                  attrs=None, **kwargs):
    results = wireviz.parse(source, return_types="svg")
    return results.decode("utf-8")
