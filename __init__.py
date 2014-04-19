'''menuData
act={name:mGeo exporter,action:show()}
'''
'''moduleInfo
Pipline exporter Maya to Houdini
'''
# mGeo Exporter v1.0
# By PaulWinex (paulwinex@gmail.com http://paulwinex.blogspot.ru) 2013
# Much thanks for the help:
#   Somesanctus (somesanctus.blogspot.ru)
# This product is not licensed

# Using:
# 1. Copy folder pw_mGeo to the PYTHONPATH folder ( <mayaInstallFolder>\Python\Lib\site-packages )
# 2. In ScriptEditor execute code:
#import pw_mGeo
#pw_mGeo.show()

def show():
    from . import mGeo
    reload(mGeo)
    mGeo.show()
