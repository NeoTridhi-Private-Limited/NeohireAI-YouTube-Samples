# Git and Scion, Video 1: Why Scion exists

Scion is Anthropic's in-house version control system. It is not released and its `scn` client has no published
commands, so nothing here uses Scion. These are plain Git commands that show Git's own design: every clone
carries the full history, content gets its name from its hash, and a shallow clone is a small step towards
"fetch only what you need".

Folders:
- `dosa-app/` : the sample repo (5 commits). `user.name` and `user.email` are set inside this repo only.
- `laptop-copy/` : a full clone made in the video.
- `slim-copy/` : a shallow clone (depth 1) made in the video.

Delete `laptop-copy/` and `slim-copy/` to try the commands yourself. Your commit hashes will differ.
No network is used: all clones are from the local folder.

## Commands to try (run from this folder, in Git Bash or any POSIX shell)

```bash
# 1. A full clone has the whole history, offline
git clone dosa-app laptop-copy
cd laptop-copy
git log --oneline
git rev-list --count HEAD        # 5
cd ..

# 2. Content-addressed: same content, same hash, always
cd dosa-app
echo "masala dosa" | git hash-object --stdin
echo "masala dosa" | git hash-object --stdin
git cat-file -p HEAD             # tree, parent, author, message
cd ..

# 3. A shallow clone copies only the latest commit
git clone --depth 1 "file://$(pwd)/dosa-app" slim-copy
git -C slim-copy rev-list --count HEAD   # 1
git -C slim-copy log --oneline
```

(`--depth` needs a `file://` URL for local clones; with a plain path Git ignores it.)

## How the sample repo was made

```bash
git init -b main dosa-app && cd dosa-app
git config user.name "Rahul"
git config user.email "rahul@example.com"
git config core.autocrlf false   # Windows only: avoids LF/CRLF warnings, local to this repo
# then five small commits: README.md, menu.py, order.py, two edits
```

Source for the Scion facts: Anthropic engineering, "Redesigning source control" (13 October 2026),
https://www.anthropic.com/engineering/redesigning-source-control
