# PyBox

現状ホームディレクトリにしか作動しないので以下の通りに配置してください

Currently it only works in the home directory, so please place it as follows

### /home/username/PyBox/README.md


## Description
システム上にPythonが動作する仮想的な環境を作るvenvをsudo[superuser do / substitute user do]　の権限を持った状態かつ、active状態にせず実行することができるツール

現時点では、独自に仮想環境を作成する。また、一つの仮想環境しか扱えない

A tool that allows you to run venv, which creates a virtual environment for Python to run on your system, with sudo[superuser do / substitute user do] privileges and without being in the active state.

At present, it creates its own virtual environment. Also, it can only handle one virtual environment.

## Dependencies
DebianベースのLinuxディストリビューション(macOS含め)活、Bashが入ってる環境でしか動かない。
また、以下にあるPythonの機能、ライブラリに依存してある。

It only runs on Debian-based Linux distributions and macOS too, Include Those needs Bash.
It also depends on the Python features and libraries listed below.

- Python >> [venv](https://docs.python.org/ja/3/library/venv.html)
  
- Python >> [pip](https://pip.pypa.io/en/stable/)

## Contributing
PyBoxをより使いやすくするために共に開発してくれる人を大歓迎しています。

We welcome anyone who is willing to develop with us to make PyBox easier to use.

## Building

インストールを始める前にファイルの権限を与えてください

Give a permission

```
chmod +x ~/PyBox/setup.py ~/PyBox/pybox ~/PyBox/setup/install ~/PyBox/setup/uninstall
```

### Set Environment variable

.bash_profile or .bashrc に下記を書き加えてください

Apped to .bash_profile or .bashrc
```
export PATH=$HOME/PyBox/pyboxenv/bin:$PATH
export PATH=$HOME/PyBox:$PATH
```


## setup.py options

Install
```command
python3 ~/PyBox/setup.py install version-3
or
python ~/PyBox/setup.py install version-default
```
uninstall 
```command
python3 ~/PyBox/setup.py uninstall
or
python ~/PyBox/setup.py uninstall
```
Check version of pyboxenv
```command
python3 ~/PyBox/setup.py status
or
python ~/PyBox/setup.py status
```

See manuals
```command
python3 ~/PyBox/setup.py manual
or
python ~/PyBox/setup.py manual
```

## Examples

Setup.py arguments

RUN
```command
pybox run file.py        #run python file
```

Using pip
```command
pybox run -m pip freeze          #use pip
```

Interactive mode
```command
pybox interactive
```

## Argument

***Python has already finished support for pip. So you can't use python2***

python3 setup.py :

commands
[ install ] <- Start install

    [install options]
    [ version-3 ] <- python version 3.~
    [ version-default ] <- python <- using default python version
    * Python has already finished support for pip. So you can't use python2

[ uninstall] <- Start uninstall

[ status] <- Check version of pyboxenv

[ manual ]  <- Open a manual



##############################################################################

pybox commands[interactive, run]  options[]:


commands

[ run ] <- run a file

    Second argument
    [ file ] <- python file
    
    example
    
    pybox run file.py

    Second argument
    - same pip arguments

    example 
    
    pybox run -m pip freeze
