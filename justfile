#!/usr/bin/env just --justfile

alias w := watch-example

watch-example n:
  watchfiles 'python examples/{{n}}.py' examples/
