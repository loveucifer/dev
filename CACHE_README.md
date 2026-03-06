# Friends Profile Cache

This system caches GitHub profile data to avoid API rate limits.

## How it works

1. **profiles_cache.json** - Contains cached profile data for all friends
2. **friends.txt** - List of GitHub usernames  
3. **generate_profiles.py** - Script to update the cache (run when adding new friends)

## Loading Strategy

1. Try to load from `profiles_cache.json` (instant, no rate limits)
2. Fallback to GitHub API if cache fails (slow, rate limited)
3. Show error message if both fail

## Updating the Cache

When adding new friends:
1. Add username to `friends.txt`
2. Run `python3 generate_profiles.py` to update cache
3. Commit both files

## Benefits

- **Fast loading** - No API calls needed
- **No rate limits** - Works even with many friends  
- **Reliable** - Always works, even offline
- **Fallback** - Still works if cache is missing