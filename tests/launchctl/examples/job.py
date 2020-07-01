#!/usr/bin/env python
import launchctl

for label in ["com.apple.Finder", "not-existing"]:
    data = launchctl.job(label)
    print(data)
