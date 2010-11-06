"""==========================================================================
views_base_pages.py

Handles various page renders 
============================================================================="""
#Import everything from the views_util
from views_util import *

"""=============================================================================

Functions

============================================================================="""
"""--------------------------------------
home: renders the home page
-----------------------------------------"""
@render_to('vasir_site/home.html')
def home(request):
    return {}