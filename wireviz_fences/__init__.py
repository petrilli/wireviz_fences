"""Top-level package for Wireviz Fences."""
import re
from wireviz import wireviz

__author__ = """Christopher Petrilli"""
__email__ = 'petrilli@amber.org'
__version__ = '0.1.0'

def fence_wireviz(source, language, css_class, options, md, classes=None, id_value='',
                  attrs=None, **kwargs):
    results = wireviz.parse(source, return_types="svg")

    # Turn it into one long string
    raw = results.decode("utf-8")
    raw = raw.replace("\n", "")

    # Strip off the XML header nonsense because we're going to embed in
    # HTML
    try:
        svg_only = re.match(r""".*(\<svg.*)""", raw)[1]
        return svg_only
    except:
        return "FAILED_PARSE"
    
