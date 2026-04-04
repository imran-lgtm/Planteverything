[app]
title = Plant Doctor
package.name = plantdoctor
package.domain = org.imran.djz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.3

# ✅ No spaces after commas
requirements = python3,kivy==2.3.0,requests,urllib3,charset-normalizer,idna,certifi

# ✅ Simple permissions
android.permissions = INTERNET

# ✅ SDK/NDK settings
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# ✅ Remove duplicate and empty lines
# android.ndk_path = (yeh line hatado)

# ✅ Remove deprecated lines
# p4a.branch = master (yeh hatado)
# android.entrypoint = main.py (yeh hatado)

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
