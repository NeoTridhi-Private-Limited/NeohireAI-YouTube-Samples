# Git and Scion, Video 2: Git from zero to GitHub

A college project's attendance app, built step by step with plain Git. Every command shown in the video was run
here with Git 2.55 and the output on screen is the real output (trimmed). Your commit hashes and dates will differ.
Nothing is pushed: the GitHub remote is added but never contacted.

Folder: `attendance-app/` is the finished repo from the video. To try it yourself, start in an empty folder.

## Commands to try (Git Bash or any POSIX shell)

```bash
# Start, with settings kept inside this repo only (no --global)
git init -b main attendance-app
cd attendance-app
git config user.name "Rahul"
git config user.email "rahul@example.com"
# Windows only, optional: avoid LF/CRLF warnings in this repo
git config core.autocrlf false

# First commit
echo "# Attendance App" > README.md
git status --short
git add README.md
git commit -m "Start the attendance app"
git status

# Branch, switch, merge (fast-forward)
git switch -c login
printf 'def login(roll_no):\n    return roll_no.isdigit()\n' > login.py
git add login.py
git commit -m "Add student login"
git switch main
git merge login
git branch

# A merge conflict: two branches change the same line
printf 'CLASS_START = "9:00"\n' > timetable.py
git add timetable.py && git commit -m "Add the timetable"
git switch -c late-start
printf 'CLASS_START = "9:30"\n' > timetable.py
git commit -am "Start at 9:30"
git switch main
printf 'CLASS_START = "8:45"\n' > timetable.py
git commit -am "Start at 8:45"
git merge late-start          # CONFLICT
cat timetable.py              # shows <<<<<<< ======= >>>>>>> markers

# Fix it: a human decides
git status --short            # UU timetable.py
echo 'CLASS_START = "9:15"' > timetable.py
git add timetable.py
git commit -m "Merge late-start, start at 9:15"
git log --oneline --graph -6

# Rebase a branch onto the latest main
git switch -c reports
printf 'def report(present, total):\n    return round(100 * present / total)\n' > report.py
git add report.py && git commit -m "Add attendance report"
git switch main
printf '# Attendance App\nA college project to mark attendance.\n' > README.md
git commit -am "Describe the project"
git switch reports
git rebase main
git log --oneline --graph -3

# Remote (not contacted in the video)
git switch main
git merge reports
git remote add origin https://github.com/rahul/attendance-app.git
git remote -v
# git push -u origin main     # not run here: needs your own GitHub repo and network

# Tag a release
git tag -a v1.0 -m "First release for the college demo"
git tag

# Undo a bad change in public
printf 'def report(present, total):\n    return 100 * present // total\n' > report.py
git commit -am "Round reports down"
git revert --no-edit HEAD
git log --oneline -3
cat report.py
```

## Pull request flow on GitHub (described in the video, not run)
Push your branch, open a pull request into main, teammates review, automatic checks run, merge when both pass,
delete the branch. GitLab calls the same thing a merge request.

Sources: git-scm.com/docs, docs.github.com, docs.gitlab.com. Scion (Anthropic, "Redesigning source control",
13 October 2026) is not public, so nothing here uses it.
