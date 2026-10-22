# Video 3: From commit to deployment (Git and Scion, NeoTridhi)

Everything here was really run with Git 2.55 on Windows (Git Bash). No network, nothing pushed.
The user name and email are set inside each repo only (never `--global`). Each repo also has
`git config core.autocrlf false` so line endings stay as written.

## Folders
- `feeapp/` : a small food-app fee calculator with tests (`fee.py`, `test_fee.py`, `build.py`, `deploy.py`)
  and two pipeline files (not run here, the hosts run them on push):
  - `.github/workflows/ci.yml` : GitHub Actions, test and build on every push and pull request, deploy on main
    (environment `production`, secret `DEPLOY_TOKEN`)
  - `.gitlab-ci.yml` : the same pipeline in GitLab C I (stages test, build, deploy; deploy only on the default branch)
- `make_bigrepo.sh` : builds `bigrepo/`, a pretend food-delivery monorepo (403 commits, an old 6 MB video committed and deleted)
- `full/`, `shallow/`, `partial/`, `sparse/` : the clones made from `bigrepo/`

## Commands to try
```sh
# the app repo
cd feeapp
git init -b main
git config user.name "Rahul"
git config user.email "rahul@example.com"
git add .
git commit -m "Add fee app, tests and pipelines"
git switch -c cap-fee            # then edit fee.py: cap the fee at 99
git commit -am "Cap the delivery fee at 99"
git switch main
git merge --no-ff cap-fee -m "Merge PR: cap the fee"
git tag -a v1.0.0 -m "First release"
git log --oneline --graph --decorate
python -m unittest -v            # the tests the pipelines run
cd ..

# big-repo tricks (from this folder)
sh make_bigrepo.sh
git -C bigrepo rev-list --count HEAD
git -C bigrepo count-objects -vH
git clone -q file://$PWD/bigrepo full
git clone -q --depth 1 file://$PWD/bigrepo shallow
git -C shallow rev-list --count HEAD
du -sh full/.git shallow/.git
git clone -q --filter=blob:none file://$PWD/bigrepo partial   # bigrepo has uploadpack.allowFilter=true
git -C partial rev-list --count HEAD
du -sh partial/.git
git -C partial log --oneline -1 -- media
git clone -q --filter=blob:none --sparse file://$PWD/bigrepo sparse
cd sparse && git sparse-checkout set services/payments && git sparse-checkout list && ls
```
`scalar clone <url>` (ships with Git) sets up partial clone, sparse checkout and background maintenance for a big repo;
it was not run here because it registers scheduled maintenance on the machine.

Scion (Anthropic's in-house system) is not released and has no public commands; nothing here uses it.
