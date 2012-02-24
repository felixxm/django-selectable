"""
django-selectable is a collection of tools and widgets for using/creating auto-complete selection widgets using Django and jQuery UI.
"""

__version_info__ = {
    'major': 0,
    'minor': 3,
    'micro': 1,
    'releaselevel': 'final',
}

def get_version():
    """
    Return the formatted version information
    """
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s' % __version_info__)
    return ''.join(vers)

__version__ = get_version()
