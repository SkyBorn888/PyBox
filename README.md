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
DebianベースのLinuxディストリビューションでしか動かない。
また、以下にあるPythonの機能、ライブラリに依存してある。

It only runs on Debian-based Linux distributions.
It also depends on the Python features and libraries listed below.

- Python >> [venv](https://docs.python.org/ja/3/library/venv.html)
  
- Python >> [pip](https://pip.pypa.io/en/stable/)

## Contributing
PyBoxをより使いやすくするために共に開発してくれる人を大歓迎しています。バグをissueに書いてもらえると嬉しいです。
We welcome anyone who is willing to develop with us to make PyBox easier to use.

## Building

インストールを始める前にファイルの権限を与えてください
Give a permission
```
chmod 755 ~/PyBox/setup.py ~/PyBox/pybox ~/PyBox/setup/install ~/PyBox/setup/uninstall

```

Install
```command
python3 setup.py install py3
or
python setup.py install py
```
uninstall 
```command
python3 setup.py uninstall
or
python setup.py uninstall
```

## Examples

Setup.py arguments

Check version of pyboxenv
```command
python3 setup.py status
or
python setup.py status
```

See manuals
```command
python3 setup.py manual
or
python setup.py manual
```




RUN
```command
pybox run file.py        #run python file
```

Using pip
```command
pybox -p freeze          #use pip
```

## Argument

***Python has already finished support for pip. So you can't use python2***

python3 setup.py :

commands
[ install ] <- Start install

    [install options]
    [ py3 ] <- python version 3.~
    [ py ] <- python <- using default python version
    * Python has already finished support for pip. So you can't use python2

[ uninstall] <- Start uninstall

[ status] <- Check version of pyboxenv

[ manual ]  <- Open a manual



##############################################################################

pybox commands[-p, run]  options[]:


commands

[ run ] <- run a file

    Second argument
    [ file ] <- python file
    
    example
    
    pybox run file.py

options
[ -p ] <- you can use pip

    Second argument
    - same pip arguments


    example 
    
    pybox -p freeze
