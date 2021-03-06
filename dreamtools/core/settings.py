# -*- python -*-
#
#  This file is part of DreamTools software
#
#  Copyright (c) 2014-2015 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.org/dreamtools
#
##############################################################################
"""Tools to handle a configuration file."""
import os
import appdirs


__all__ = ["DreamToolsConfig"]


# first item if the value
# second item if a type or TUPLE of types possible
# third item is documentation

class DreamToolsConfig(object):

    def __init__(self):
        #super(DreamToolsConfig, self).__init__(name="dreamtools",
        #        default_params=defaultParams)
        print("Welcome to DreamTools")
        print("\nUsage example:")
        print(">>> from dreamtools import D2C1")
        print(">>> c = D2C1()")
        print(">>> filename = c.download_template")
        print(">>> c.score(filename)")
        self.appdirs = appdirs.AppDirs("dreamtools")
    
    def _get_config_dir(self):
        sdir = self.appdirs.user_config_dir
        return self._get_and_create(sdir)
    user_config_dir = property(_get_config_dir,
            doc="return directory of this configuration file")
    def _get_and_create(self, sdir):
        if not os.path.exists(sdir):
            print("Creating directory %s " % sdir)
            try:
                self._mkdirs(sdir)
            except Exception:
                print("Could not create the path %s " % sdir)
                return None
        return sdir
    
    def _mkdirs(self, newdir, mode=0o777):
        """from matplotlib mkdirs

        make directory *newdir* recursively, and set *mode*.  Equivalent to ::

        > mkdir -p NEWDIR
        > chmod MODE NEWDIR
        """
        try:
            if not os.path.exists(newdir):
                parts = os.path.split(newdir)
                for i in range(1, len(parts) + 1):
                    thispart = os.path.join(*parts[:i])
                    if not os.path.exists(thispart):
                        os.makedirs(thispart, mode)

        except OSError as err:
            # Reraise the error unless it's about an already existing directory
            if err.errno != errno.EEXIST or not os.path.isdir(newdir):
                raise





