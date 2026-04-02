[app]
title = PlantEverything
package.name = planteverything
package.domain = org.imran
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
p4a.branch = master
# (list) Permissions
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) App Title
title = Plant Encyclopedia

# (str) Package name
package.name = plantencyclopedia
[buildozer]
log_level = 2
warn_on_root = 1
