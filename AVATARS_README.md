# Local Avatar System 🖼️

This system stores friend avatars locally to avoid GitHub API rate limits and improve loading speed.

## How it works

1. **avatars/** - Directory containing all friend avatar images
2. **download_avatars.py** - Script to download/update avatars
3. **profiles_cache.json** - Uses local paths (`avatars/username.png`)
4. **GitHub Actions** - Auto-updates avatars weekly and on friends.txt changes

## Benefits

✅ **No API limits** - No more "temporarily unavailable" messages  
✅ **Faster loading** - Local images load instantly  
✅ **Always works** - No external dependencies  
✅ **Auto-updates** - CI/CD keeps avatars fresh  

## Adding New Friends

1. Add username to `friends.txt`
2. Run `python3 download_avatars.py` (or let CI/CD do it)
3. Commit and push

## Manual Avatar Update

```bash
python3 download_avatars.py
```

## GitHub Actions

- **Triggers**: Push to friends.txt, weekly schedule, manual
- **Actions**: Downloads new avatars, updates cache, commits changes
- **Frequency**: Automatic weekly updates to keep avatars fresh