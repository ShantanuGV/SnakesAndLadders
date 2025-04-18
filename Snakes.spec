# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Snakes', 'and', 'Ladder.py'],
    pathex=[],
    binaries=[],
    datas=[('101692.jpg', '.'), ('100.png', '.'), ('pin_red.png', '.'), ('pin_blue.png', '.'), ('dice_1.png', '.'), ('dice_2.png', '.'), ('dice_3.png', '.'), ('dice_4.png', '.'), ('dice_5.png', '.'), ('dice_6.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Snakes',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
