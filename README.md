<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/launchctl.svg?maxAge=3600)](https://pypi.org/project/launchctl/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/launchctl.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/launchctl.py/actions)

### Installation
```bash
$ [sudo] pip install launchctl
```

#### Examples
```python
import launchctl

for job in launchctl.jobs():
    print("%s %s %s" % (job.pid if job.pid else "", job.status, job.label))

launchctl.job("com.apple.Finder")
{...}
```

#### Related
+   [`launchd-env` - launchd.plist environment variables](https://pypi.org/project/launchd-env/)
+   [`launchd-exec` - execute script via launchd](https://pypi.org/project/launchd-exec/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`launchd-logs` - launchd.plist logs](https://pypi.org/project/launchd-logs/)
+   [`launchctl.py`](https://pypi.org/project/launchctl/)

#### Links
+   [launchctl Man Page](https://ss64.com/osx/launchctl.html)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
