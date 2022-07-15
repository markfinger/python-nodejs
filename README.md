## PyPI Warning
**Note that the `nodejs` package on PyPI has been passed on to another user that is actively bundling node binaries. See https://github.com/samwillis/nodejs-pypi for more information.**

**If you want to use the legacy version of this package, you can install it with `pip install nodejs==0.1.1` or pin it to `nodejs==0.1.1` in your requirements.txt.**

python-nodejs
=============

[![Build Status](https://travis-ci.org/markfinger/python-nodejs.svg?branch=master)](https://travis-ci.org/markfinger/python-nodejs)

Python bindings and utils for [Node.js](http://nodejs.org) and [io.js](https://iojs.org/).

```python
from nodejs.bindings import node_run

stderr, stdout = node_run('/path/to/some/file.js', '--some-argument')
```

Installation
------------

```
pip install nodejs==0.1.1
```


Bindings
--------

### nodejs.bindings.node_run()

Invokes Node with the arguments provided and return the resulting stderr and stdout.

```python
from nodejs.bindings import node_run

stderr, stdout = node_run('/path/to/some/file.js', '--some-argument')
```

### nodejs.bindings.ensure_installed()

Raises an exception if node is not installed.

### nodejs.bindings.ensure_version_gte()

Raises an exception if the installed version of node is less than the version required.

Arguments:

`version_required`: a tuple containing the minimum version required.

```python
from nodejs.bindings import ensure_node_version_gte

ensure_node_version_gte((0, 10, 0,))
```

### nodejs.bindings.is_installed

A boolean indicating if Node is installed.

### nodejs.bindings.version

A tuple containing the version of Node installed. For example, `(0, 10, 33)`

### nodejs.bindings.version_raw

A string containing the raw version returned from Node. For example, `'v0.10.33'`



Running the tests
-----------------

```bash
mkvirtualenv python-nodejs
pip install -r requirements.txt
nosetests
```
