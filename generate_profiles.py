#!/usr/bin/env python3
"""
Script to fetch GitHub profile data and cache it locally.
Run this occasionally to update the profile cache.
"""

import json
import requests
import time
from pathlib import Path


def fetch_github_profiles():
    # Read friends list
    friends_file = Path("friends.txt")
    if not friends_file.exists():
        print("friends.txt not found!")
        return

    friends = []
    with open(friends_file, "r") as f:
        friends = [line.strip() for line in f if line.strip()]

    profiles = {}

    print(f"Fetching profiles for {len(friends)} friends...")

    for i, username in enumerate(friends, 1):
        print(f"[{i}/{len(friends)}] Fetching {username}...")

        try:
            # Add delay to avoid rate limiting
            if i > 1:
                time.sleep(1)

            response = requests.get(
                f"https://api.github.com/users/{username}", timeout=10
            )

            if response.status_code == 200:
                user_data = response.json()
                # Store only the data we need
                profiles[username] = {
                    "login": user_data["login"],
                    "avatar_url": user_data["avatar_url"],
                    "html_url": user_data["html_url"],
                    "name": user_data.get("name", user_data["login"]),
                }
                print(f"  ✓ Success: {user_data['login']}")
            else:
                print(f"  ✗ Failed: {response.status_code}")

        except Exception as e:
            print(f"  ✗ Error fetching {username}: {e}")

    # Write the cache file
    cache_file = Path("profiles_cache.json")
    with open(cache_file, "w") as f:
        json.dump(profiles, f, indent=2)

    print(f"\n✅ Generated cache with {len(profiles)} profiles")
    print(f"Cache saved to: {cache_file}")

    # Generate timestamp
    timestamp_file = Path("profiles_timestamp.txt")
    with open(timestamp_file, "w") as f:
        f.write(str(int(time.time())))

    return profiles


if __name__ == "__main__":
    fetch_github_profiles()
