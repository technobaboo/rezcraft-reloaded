import bpy
import os
import re

os.chdir(bpy.path.abspath("//"))

def glob_re(pattern, strings):
    return filter(re.compile(pattern).match, strings)

for f in glob_re(r'.+\.png[0-9]{4}$', os.listdir()):
    os.rename(f, f[0:-4])
