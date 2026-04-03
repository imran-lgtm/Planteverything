[app]
title = Plant Encyclopedia
package.name = plantencyclopedia
package.domain = org.imran.djz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requirements (Crash Fix for Android 12+)
requirements = python3, kivy==2.3.0, requests, urllib3, charset-normalizer, idna, certifi, openssl, hostpython3

orientation = portrait
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
android.manifest.attributes = android:usesCleartextTraffic="true"
android.allow_backup = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
