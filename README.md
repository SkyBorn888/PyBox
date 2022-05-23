# Pydo

## Description
システム上にPythonが動作する仮想的な環境を作るvenvをsudo[superuser do / substitute user do]　の権限を持った状態かつ、active状態にせず実行することができるツール

現時点では、独自に仮想環境を作成する。また、一つの仮想環境しか扱えない

## Dependencies
Linuxディストリビューション上でしか動かない。
また、以下にあるPythonの機能、ライブラリに依存してある。

- Python >> [venv](https://docs.python.org/ja/3/library/venv.html)
  
- Python >> [pip](https://pip.pypa.io/en/stable/)

## Contributing
Pydoをより使いやすくするために共に開発してくれる人を大歓迎しています。Pull request, Issueを使ってバグや拡張機能のコードなどを書いてもらえると嬉しいです。

## Example

Install
```command
python3 setup.py install py3
python setup.py install py
```
uninstall 
```command
python3 setup.py uninstall
python setup.py uninstall
```
Check version of pydoenv
```command
python3 setup.py status
python setup.py status
```
RUN
```command
pydo file.py        #run python file
pydo -m pip freeze  #use pip
```

## Argument
python3 setup.py ~ ~:

First argument
[ install ] <- Start install
    Second argument
    [ py3 ] <- python version 3.~
    [ py ] <- python <- using default python version
  ***Python has already finished support for pip. So you can't use python2***

[ uninstall] <- Start uninstall

[ status] <- Check version of pydoenv

[ manual ]  <- Open a manual
