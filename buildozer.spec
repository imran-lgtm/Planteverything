[app]
# App ka naam
title = Plant Doctor

# Package name
package.name = plantdoctor

# Domain
package.domain = org.imran.djz

# Source code kahan hai
source.dir = .

# Main file extensions
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# Version
version = 1.0

# Requirements (libraries)
requirements = python3, kivy==2.3.0, requests, urllib3, charset-normalizer, idna, certifi, openssl, hostpython3

# Permissions
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android API Settings (Ab sirf EK baar hain)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# Architecture
android.archs = arm64-v8a, armeabi-v7a

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
