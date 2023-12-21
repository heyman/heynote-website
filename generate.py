import json
import re

from jinja2 import Environment, FileSystemLoader


env = Environment(
    loader=FileSystemLoader(".")
)
template = env.get_template("index.html")


with open("releases.json", "r") as f:
    all_releases = json.load(f)

#print("count:", len(all_releases))
#from pprint import pprint
#pprint(all_releases[0])


releases = []
prereleases = []
for release in all_releases:
    if release["draft"]:
        continue
    
    #print(release["name"])
    release_data = {
        "version": release["name"],
        "mac_universal": None,
        "mac_arm": None,
        "mac_intel": None,
        "windows": None,
        "linux_appimage": None,
        "linux_snap": None,
    }
    regex_first_part = r"^Heynote_\d+\.\d+\.\d+(-(beta|alpha)(\.\d*)?)?"
    for asset in release["assets"]:
        #print("-->", asset["name"])
        if re.match(regex_first_part + r"_universal\.dmg$", asset["name"]):
            release_data["mac_universal"] = asset["browser_download_url"]
        elif re.match(regex_first_part + r"_arm64\.dmg$", asset["name"]):
            release_data["mac_arm"] = asset["browser_download_url"]
        elif re.match(regex_first_part + r"_x64\.dmg$", asset["name"]):
            release_data["mac_intel"] = asset["browser_download_url"]
        elif re.match(regex_first_part + r"\.exe$", asset["name"]):
            release_data["windows"] = asset["browser_download_url"]
        elif re.match(regex_first_part + r"_x86_64\.AppImage$", asset["name"]):
            release_data["linux_appimage"] = asset["browser_download_url"]
        elif re.match(regex_first_part + r"_amd64\.snap$", asset["name"]):
            release_data["linux_snap"] = asset["browser_download_url"]
    
    if release["prerelease"]:
        prereleases.append(release_data)
    else:
        releases.append(release_data)
    #print(release_data)

with open("./_site/index.html", "w") as f:
    f.write(template.render(
        releases=releases,
        prereleases=prereleases,
    ))
