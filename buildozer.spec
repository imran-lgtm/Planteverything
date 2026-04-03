[app]
title = Plant Doctor
package.name = plantdoctor
package.domain = org.imran.djz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.1

requirements = python3, kivy==2.3.0, requests, urllib3, charset-normalizer, idna, certifi

android.permissions = INTERNET, CAMERA
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
