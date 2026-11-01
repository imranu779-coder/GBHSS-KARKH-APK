[app]
title = GBHS App
package.name = gbhsapp
package.domain = com.gbhs.gbhsapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
android.ndk = 25b
android.accept_sdk_license_agreements = True
