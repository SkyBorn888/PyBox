# Pydo

## Description
システム上にPythonが動作する仮想的な環境を作るvenvをsudo[superuser do / substitute user do]　の権限を持った状態かつ、active状態にせず実行することができるツール

現時点では、独自に仮想環境を作成する。また、一つの仮想環境しか扱えない

## Dependencies
DebianベースのLinuxディストリビューションでしか動かない。
また、以下にあるPythonの機能、ライブラリに依存してある。

- Python >> [venv](https://docs.python.org/ja/3/library/venv.html)
  
- Python >> [pip](https://pip.pypa.io/en/stable/)

## Contributing
Pydoをより使いやすくするために共に開発してくれる人を大歓迎しています。バグをissueに書いてもらえると嬉しいです。


## Building

インストールを始める前にファイルの権限を与えてください

Give a permission
```
chmod 755 ~/Pydo/setup.py ~/Pydo/pydo ~/Pydo/setup/install ~/Pydo/setup/uninstall

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

## Example

Setup.py arguments

Check version of pydoenv
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
pydo run file.py        #run python file
```

Using pip
```command
pydo -p freeze          #use pip
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

[ status] <- Check version of pydoenv

[ manual ]  <- Open a manual



##############################################################################

pydo commands[-p, run]  options[]:


commands

[ run ] <- run a file

    Second argument
    [ file ] <- python file
    
    example
    
    pydo run file.py

options
[ -p ] <- you can use pip

    Second argument
    - same pip arguments


    example 
    
    pydo -p freeze
