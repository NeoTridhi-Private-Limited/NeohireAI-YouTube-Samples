# Git and Scion, Video 5: the future (sample)

Scion is Anthropic's in-house version control system. It is not released and its `scn` commands are not public,
so nothing here uses Scion. These are plain Git (2.55) commands that show Scion's ideas in a small way.
Commit hashes on your machine will differ.

## What is here
- `foodapp/` : a small food-delivery monorepo (services/orders, services/payments, services/riders, apps/android, docs).
  `user.name` / `user.email` are set in this repo only (`git config`, never `--global`).
- `orders-only/` : a sparse clone that checks out only `services/orders`.
- `lazy/` : a partial clone (`--filter=blob:none`) that fetches file contents on demand.
- `.github/workflows/agent-ci.yml` : a GitHub Actions workflow for agent branches (not run here: GitHub runs it on push).

## Commands to try (from this folder)

Sparse checkout, only one folder on disk:

    git clone --no-checkout foodapp orders-only
    cd orders-only
    git sparse-checkout set services/orders
    git checkout main
    ls
    ls services
    cd ..

Partial clone, file contents fetched on demand (the source repo has `uploadpack.allowFilter true`):

    git clone --filter=blob:none --no-checkout file://$PWD/foodapp lazy
    cd lazy
    git rev-list --objects --all --missing=print | grep -c '^?'
    git checkout main
    git rev-list --objects --all --missing=print | grep -c '^?'
    cd ..

Worktrees, one folder and one branch per agent:

    cd foodapp
    git worktree add ../agent-orders -b agent/orders
    git worktree add ../agent-payments -b agent/payments
    git branch
    # each "agent" makes one commit in its own folder, then:
    git merge agent/orders
    git merge --no-edit agent/payments
    git log --oneline --graph
    git worktree remove ../agent-orders
    git worktree remove ../agent-payments
    git branch -d agent/orders agent/payments

Give a branch a better name than final-final-fix:

    git switch -c final-final-fix
    git branch -m fix/upi-timeout
    git branch --show-current
    git switch main

(If you re-run these, delete `orders-only/` and `lazy/` first, and use new branch names.)
No network is needed; nothing is pushed anywhere.
