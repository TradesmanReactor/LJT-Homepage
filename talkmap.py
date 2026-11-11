#!/usr/bin/env bash
set -euo pipefail

rm -rf files talkmap markdown_generator scripts _data/comments
rm -f talkmap.ipynb talkmap_out.ipynb
rm -f images/bio-photo.jpg images/bio-photo-2.jpg images/editing-talk.png images/profile.png
rm -rf images/themes images/wiki

npm install -g uglify-js
uglifyjs assets/js/plugins/jquery.greedy-navigation.js assets/js/_main.js assets/js/theme.js -c -m -o assets/js/main.min.js
bundle exec jekyll build --baseurl "/LJT-Homepage"

test -s _site/index.html
test -s _site/publications/index.html
test -s _site/publications/synlogic/index.html
grep -qF "Junteng Liu" _site/index.html
grep -qF "Professor Junxian He" _site/index.html
grep -qF "MINIMAX" _site/index.html
grep -qF "Shanghai AI Lab" _site/index.html
grep -qF "SynLogic" _site/index.html
grep -qF "Perception Bottleneck" _site/index.html
grep -qF "Universal Truthfulness Hyperplane" _site/index.html
grep -qF "In-Context Sharpness" _site/index.html
grep -qF "C-Eval" _site/index.html
grep -qF "Composing Parameter-Efficient" _site/index.html
grep -qF "Zhiyuan Honor Scholarship" _site/index.html
grep -qF "jliugi@connect.ust.hk" _site/index.html
grep -qF "Vicent0205" _site/index.html
grep -qF "tbK9jl4AAAAJ" _site/index.html
grep -qF "junteng88716710" _site/index.html
grep -qF "SynLogic" _site/publications/index.html
grep -qF "Composing Parameter-Efficient Modules with Arithmetic Operations" _site/publications/index.html
test ! -e _site/talkmap
test ! -e _site/files
