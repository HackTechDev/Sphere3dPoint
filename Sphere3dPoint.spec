# -*- mode: python -*-
a = Analysis(['Sphere3dPoint.py'],
             pathex=['/home/solomonkane/PYTHON/Sphere3dPoint'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Sphere3dPoint',
          debug=False,
          strip=None,
          upx=True,
          console=True )
