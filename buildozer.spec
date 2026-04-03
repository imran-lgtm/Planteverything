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
# (list) Android additionnal libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android-v7/libgnustl_shared.so

# (str) XML attribute to add to the application element in the manifest
android.manifest.attributes = android:usesCleartextTraffic="true"

# (list) Android application meta-data to set (name=value format)
#android.meta_data =
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
