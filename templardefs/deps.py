'''
dependencies for this project
'''

def populate(d):
    d.packs=[
        # for creating the interfaces
        'swig',
        # for the examples
        'swig-examples',
        # for the documentation
        'swig-doc',
        # for development
        'gcc-doc',
        # for swig file
        'autoconf-archive',
    ]

def getdeps():
    return [
        __file__, # myself
    ]
