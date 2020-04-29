import hashlib
import zipfile
import json
import os

os.chdir("..")
z = zipfile.ZipFile("files/data/config_fb_tr.zip", mode="w")
for root, dirs, files in os.walk("config_fb_tr"):
    for file in files:
        z.write(os.path.join(root, file),
                arcname=os.path.join(root,
                                     file).split("config_fb_tr/")[1])
z.close()
with open("files/data/config_fb_tr.zip", mode="rb") as f:
    hash_ = hashlib.md5(f.read()).hexdigest()
os.rename("files/data/config_fb_tr.zip",
          f"files/data/config_fb_tr_{hash_}.zip")
with open("files/versions.json") as f:
    versions = json.load(f)
versions["data/config_fb_tr.zip"] = hash_
with open("files/versions.json", "w") as f:
    f.write(json.dumps(versions))
print(f"Готово, файл config_fb_tr_{hash_}.zip(уже записан в versions.json)")
