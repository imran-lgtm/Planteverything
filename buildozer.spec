[app]
# (str) Title of your application
title = Plant Encyclopedia

# (str) Package name
package.name = plantencyclopedia

# (str) Package domain
package.domain = org.imran.djz

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements (ZAROORI LINE)
requirements = python3, kivy, requests, urllib3, charset-normalizer, idna, certifi

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) Android archs
android.archs = armeabi-v7a, arm64-v8a

# (bool) Allow backup
android.allow_backup = True

# (str) python-for-android branch
p4a.branch = master

[buildozer]
# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
