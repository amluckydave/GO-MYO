from myoLib.pics.thumb_png import img as thumb_png
from myoLib.pics.six_png import img as six_png
from myoLib.pics.ok_png import img as ok_png
from myoLib.pics.peace_png import img as peace_png
from myoLib.pics.adduct_png import img as adduct_png
from myoLib.pics.abduct_png import img as abduct_png
from myoLib.pics.ring_png import img as ring_png
from myoLib.pics.fist_png import img as fist_png
from myoLib.pics.waveIn_png import img as waveIn_png
from myoLib.pics.waveOut_png import img as waveOut_png
from myoLib.pics.seven_png import img as seven_png
from myoLib.pics.relax_png import img as relax_png
from myoLib.pics.white_png import img as white_png
from myoLib.pics.allPics_png import img as allPics_png
from myoLib.pics.logo_png import img as logo_png

import os
import base64
from myoLib.myoPath import myoPath


def init_Pics():
    linkpath = myoPath()

    if not os.path.exists(linkpath + r'\thumb_png.png'):
        tmp = open(linkpath + r'\thumb_png.png', 'wb')
        tmp.write(base64.b64decode(thumb_png))
        tmp.close()

    if not os.path.exists(linkpath + r'\six_png.png'):
        tmp = open(linkpath + r'\six_png.png', 'wb')
        tmp.write(base64.b64decode(six_png))
        tmp.close()

    if not os.path.exists(linkpath + r'\ok_png.png'):
        tmp = open(linkpath + r'\ok_png.png', 'wb')
        tmp.write(base64.b64decode(ok_png))
        tmp.close()
    if not os.path.exists(linkpath + r'\peace_png.png'):
        tmp = open(linkpath + r'\peace_png.png', 'wb')
        tmp.write(base64.b64decode(peace_png))
        tmp.close()
    if not os.path.exists(linkpath + r'\adduct_png.png'):
        tmp = open(linkpath + r'\adduct_png.png', 'wb')
        tmp.write(base64.b64decode(adduct_png))
        tmp.close()
    if not os.path.exists(linkpath + r'\abduct_png.png'):
        tmp = open(linkpath + r'\abduct_png.png', 'wb')
        tmp.write(base64.b64decode(abduct_png))
        tmp.close()
    if not os.path.exists(linkpath + r'\ring_png.png'):
        tmp = open(linkpath + r'\ring_png.png', 'wb')
        tmp.write(base64.b64decode(ring_png))
        tmp.close()

    if not os.path.exists(linkpath + r'\fist_png.png'):
        tmp = open(linkpath + r'\fist_png.png', 'wb')
        tmp.write(base64.b64decode(fist_png))
        tmp.close()

    if not os.path.exists(linkpath + r'\waveIn_png.png'):
        tmp = open(linkpath + r'\waveIn_png.png', 'wb')
        tmp.write(base64.b64decode(waveIn_png))
        tmp.close()

    if not os.path.exists(linkpath + r'\waveOut_png.png'):
        tmp = open(linkpath + r'\waveOut_png.png', 'wb')
        tmp.write(base64.b64decode(waveOut_png))
        tmp.close()

    if not os.path.exists(linkpath + r'\seven_png.png'):
        tmp = open(linkpath + r'\seven_png.png', 'wb')
        tmp.write(base64.b64decode(seven_png))
        tmp.close()

    if not os.path.exists(linkpath + r'\relax_png.png'):
        tmp = open(linkpath + r'\relax_png.png', 'wb')
        tmp.write(base64.b64decode(relax_png))
        tmp.close()
    if not os.path.exists(linkpath + r'\white_png.png'):
        tmp = open(linkpath + r'\white_png.png', 'wb')
        tmp.write(base64.b64decode(white_png))
        tmp.close()

    if not os.path.exists(linkpath + r'\allPics_png.png'):
        tmp = open(linkpath + r'\allPics_png.png', 'wb')
        tmp.write(base64.b64decode(allPics_png))
        tmp.close()

    if not os.path.exists(linkpath + r'\logo_png.png'):
        tmp = open(linkpath + r'\logo_png.png', 'wb')
        tmp.write(base64.b64decode(logo_png))
        tmp.close()

    return
