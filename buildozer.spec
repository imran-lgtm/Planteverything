[app]
title = Plant Doctor
package.name = plantdoctor
package.domain = org.imran.djz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.3

requirements = python3,kivy==2.3.0,requests,urllib3,charset-normalizer,idna,certifi

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# ✅ YAHAN ADD KARO - [app] section ke end mein
android.sdk_path = ~/.buildozer/android/platform/android-sdk
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
