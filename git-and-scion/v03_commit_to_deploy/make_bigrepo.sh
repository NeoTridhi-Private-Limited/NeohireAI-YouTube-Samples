#!/bin/sh
# Builds "bigrepo": a pretend food-delivery monorepo with a long history and an
# old 6 MB video that was committed by mistake and later deleted.
# Run from this sample folder:  sh make_bigrepo.sh
set -e
rm -rf bigrepo && mkdir bigrepo && cd bigrepo
git init -q -b main
git config user.name "Rahul"
git config user.email "rahul@example.com"
git config core.autocrlf false
mkdir -p services/payments services/orders apps/android apps/ios docs
for d in services/payments services/orders apps/android apps/ios docs; do
  echo "# $d" > $d/README.md
done
git add . && git commit -q -m "Start the monorepo"
mkdir media && head -c 6000000 /dev/urandom > media/launch_video.mp4
git add . && git commit -q -m "Add launch video (oops)"
git rm -q -r media && git commit -q -m "Remove the video"
i=1
while [ $i -le 400 ]; do
  for d in services/payments services/orders apps/android apps/ios; do
    echo "change $i in $d" >> $d/notes.txt
  done
  git add . && git commit -q -m "Change $i"
  i=$((i + 1))
done
git config uploadpack.allowFilter true
git gc -q
echo "bigrepo ready"
