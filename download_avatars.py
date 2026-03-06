#!/usr/bin/env python3
"""
Download GitHub avatars and store them locally to avoid API limits.
Run this script whenever you add new friends or want to update avatars.
"""

import json
import requests
import time
from pathlib import Path


def download_avatars():
    # Read friends list
    friends_file = Path("friends.txt")
    if not friends_file.exists():
        print("❌ friends.txt not found!")
        return

    with open(friends_file, "r") as f:
        friends = [line.strip() for line in f if line.strip()]

    # Create avatars directory
    avatars_dir = Path("avatars")
    avatars_dir.mkdir(exist_ok=True)

    profiles = {}
    downloaded_count = 0

    print(f"📥 Downloading avatars for {len(friends)} friends...")

    for i, username in enumerate(friends, 1):
        print(f"[{i}/{len(friends)}] {username}...")

        avatar_path = avatars_dir / f"{username}.png"

        # Skip if already downloaded
        if avatar_path.exists():
            print(f"  ✓ Already exists: {avatar_path}")
        else:
            try:
                # Download avatar from GitHub
                response = requests.get(
                    f"https://github.com/{username}.png", stream=True, timeout=10
                )

                if response.status_code == 200:
                    with open(avatar_path, "wb") as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"  ✅ Downloaded: {avatar_path}")
                    downloaded_count += 1
                else:
                    print(f"  ❌ Failed: HTTP {response.status_code}")

            except Exception as e:
                print(f"  ❌ Error: {e}")

        # Create profile entry with local path
        profiles[username] = {
            "login": username,
            "avatar_url": f"avatars/{username}.png",  # Local path
            "html_url": f"https://github.com/{username}",
            "name": username,
        }

        # Small delay to be nice to GitHub
        if i < len(friends):
            time.sleep(0.5)

    # Update profiles cache with local paths
    cache_file = Path("profiles_cache.json")
    with open(cache_file, "w") as f:
        json.dump(profiles, f, indent=2)

    print(f"\n🎉 Complete!")
    print(f"📊 Downloaded: {downloaded_count} new avatars")
    print(f"📁 Total avatars: {len(list(avatars_dir.glob('*.png')))}")
    print(f"💾 Updated cache: {cache_file}")


if __name__ == "__main__":
    download_avatars()
