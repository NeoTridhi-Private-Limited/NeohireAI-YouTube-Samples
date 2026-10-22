# Video 4: Alternatives to GitHub and the cost (Git and Scion, NeoTridhi)

Git commands here were really run with Git 2.55 and Git LFS 3.7.1 on Windows (Git Bash). No network, nothing pushed:
the remote addresses are examples only. The user name and email are set inside the repo only (never `--global`),
plus `git config core.autocrlf false`.

## Folders and files
- `mobile/` : a bank's mobile-team helper (`emi.py`, `test_emi.py`, `deploy.py`) with three remotes, a release tag
  `v2.1.0`, and `promo.mp4` stored with Git LFS. Pipeline files (not run here, the hosts run them on push):
  - `bitbucket-pipelines.yml` : Bitbucket Pipelines, tests on every branch, deploy step (production) on main
  - `azure-pipelines.yml` : Azure Pipelines, tests, then deploy only on main (`DEPLOY_TOKEN` from a secret variable)
- `forgejo/compose.yaml` : a small self-hosted Forgejo server (not run here; Docker is not installed on the build machine)
- `mobile.bundle` : the whole `mobile` repo in one file (made before the LFS commit)
- `restored/` : a repo cloned back from the bundle

## Commands to try
```sh
cd mobile
git init -q -b main
git config user.name "Rahul"
git config user.email "rahul@example.com"
git add .
git commit -q -m "EMI module, tests, pipelines"
git remote add github git@github.com:example-bank/mobile.git
git remote add gitlab git@gitlab.com:example-bank/mobile.git
git remote add forgejo ssh://git@git.bank.test:222/mobile/app.git
git remote -v
# (a README commit and the tag: git tag -a v2.1.0 -m "Release 2.1.0")
git bundle create ../mobile.bundle --all
git bundle verify ../mobile.bundle
cd ..
git clone -q mobile.bundle restored
git -C restored log --oneline --decorate
cd mobile
git lfs install --local
git lfs track "*.mp4"
git add .gitattributes promo.mp4
git commit -q -m "Add promo video with LFS"
git lfs ls-files --size
git show --stat --format=%s HEAD
python -m unittest -v
```
Self-host (on a machine with Docker): `cd forgejo && docker compose up -d`, then open http://localhost:3000.

Sapling (`sl`) and Jujutsu (`jj`) are described in the video but not run here.
Prices in the video were read from the official pricing pages in October 2026: check the current pricing.
