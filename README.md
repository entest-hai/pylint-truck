## Setup pylint and trunk for vscode per project workspace

**04 DEC 2021 TRAN MINH HAI**

#### 1. Check python inteprepter in vscode

```
python.defaultInterpreterPath": "/usr/local/bin/python3",

```

### 2. Run pylint from vscode command

Open command mode

```
cmd shift p
```

Select linter

```
Python: Select Linter
```

ON, OFF linter

```
Python: Enable Linting
```

### 3. create .pylintrc

```
pylint --generate-rcfile > .pylintrc
```

### 4. disable checking an error by setting pylintrc

To ingore error C0103 function_name_style = snake_case, add this line to **.pylintrc**

```
disable=C0103
```

Or add into line code

```
# pylint: disable-msg=C0103
```

### 5. setup trunk
install globally 
```
curl https://get.trunk.io/ -fsSL | bash
```

check 
```
trunk check 
```