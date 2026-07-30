import requests

PLAYLISTS = [
    ("JioHotstar", "https://jhsevetns-fhd.rtxcric.workers.dev/playlist.m3u"),
    ("SonyLiv", "https://raw.githubusercontent.com/doctor-8trange/zyphora/refs/heads/main/data/sony.m3u"),
    ("FanCode", "https://raw.githubusercontent.com/doctor-8trange/zyphx8/refs/heads/main/data/fancode.m3u"),
    ("ICC", "https://raw.githubusercontent.com/doctor-8trange/nexphi0/refs/heads/main/data/icc.m3u"),
    ("Zee5", "https://raw.githubusercontent.com/doctor-8trange/quarnex/refs/heads/main/data/zee5.m3u"),
    ("Sony2","https://raw.githubusercontent.com/srhady/SonyLiv/refs/heads/main/sonyliv_playlist.m3u"),
]

OUTPUT_FILE = "playlist.m3u"

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    out.write("#EXTM3U\n")

    for name, url in PLAYLISTS:
        print(f"Merging {name}...")

        # Section separator
        out.write(f"\n# ===== {name} =====\n")

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            lines = response.text.splitlines()

            # Skip the source #EXTM3U header
            if lines and lines[0].strip().upper() == "#EXTM3U":
                lines = lines[1:]

            for line in lines:
                out.write(line + "\n")

        except Exception as e:
            print(f"Failed to merge {name}: {e}")

print("Merged playlist created successfully!")
