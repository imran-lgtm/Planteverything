[app]
# App ka naam
title = Plant Doctor

# Package name
package.name = plantdoctor

# Domain
package.domain = org.yourname

# Source code kahan hai
source.dir = .

# Main file
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# Version
version = 1.0

# Requirements (libraries)
requirements = python3,kivy,kivymd,requests,pillow,urllib3,charset_normalizer,certifi,idna

# Icon
icon.filename = %(source.dir)s/assets/icon.png

# Permissions
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# API level
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
