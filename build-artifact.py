#!/usr/bin/env python3
"""Derive artifact.html from index.html.

Claude Artifacts wrap the published file in their own <!doctype>/<html>/<head>/
<body> skeleton, so the artifact build is index.html with that wrapper removed:
<title>, <style>, the <main> mount point and <script>, nothing else.

Everything else — including the theme tokens, which already cover the bare
:root, the prefers-color-scheme media query and an explicit [data-theme]
choice — is shared, so there is only ever one copy of the game to maintain.

Usage:  python3 build-artifact.py
"""
import io
import re
import sys

SRC, OUT = "index.html", "artifact.html"

src = io.open(SRC, encoding="utf-8").read()


def grab(pattern, what):
    m = re.search(pattern, src, re.S)
    if not m:
        sys.exit("could not find %s in %s" % (what, SRC))
    return m.group(0)


title = grab(r"<title>.*?</title>", "the <title>")
style = grab(r"<style>.*?</style>", "the <style> block")
mount = grab(r'<main id="app"></main>', "the <main> mount point")
script = grab(r"<script>.*?</script>", "the <script> block")

out = "\n".join([title, style, mount, script]) + "\n"

for banned in ("<!DOCTYPE", "<html", "<head", "<body"):
    if banned.lower() in out.lower():
        sys.exit("wrapper tag %s survived the strip — refusing to write" % banned)

io.open(OUT, "w", encoding="utf-8").write(out)
print("%s -> %s  (%d bytes, %d fewer than the standalone page)"
      % (SRC, OUT, len(out), len(src) - len(out)))
