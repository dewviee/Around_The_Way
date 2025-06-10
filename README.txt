วิธีการเล่น 

เอาชีวิตรอดไปจนกว่าจะถึงวันที่ 10 และ

1. ต้องคอยกำจัดยาน alien เพราะ alien จะยิงเรา
2. เมื่อโดนยิงเลือดยานจะลด ให้ไปซ่อมที่ด้านขวา
3. เมื่อมีเสียงเตือน ให้ไปซ่อมยานที่ console ด้านซ้าย เมื่อเสร็จแล้วกด E ออก (หากไม่ซ่อมยานจะไม่เดินทาง จะหยุดอยู่อย่างนั้น)

# how to build

## Install PyInstaller:
```bash
pip install pyinstaller
```

## Install PyInstaller:
```bash
pip install pgzero
```

# Build

## Know pgzero Location

Run this command 
```bash
pip show pgzero
```

will have data like this
```
Name: pgzero
Version: 1.2.1
Summary: A zero-boilerplate 2D games framework
Home-page: http://pypi.python.org/pypi/pgzero
Author: Daniel Pope
Author-email: mauve@mauveweb.co.uk
License: UNKNOWN
Location: %LOCALAPPDATA%\programs\python\python38-32\lib\site-packages
Requires: numpy, pygame
Required-by:
```


## Build command
Take `Location` from above or `%LOCALAPPDATA%` also work 
but if not just use absolute path like `c:\somepath\programs\python\python38-32\lib\site-packages\pgzero\data;pgzero\data`
```cmd
pyinstaller --onefile ^
--add-data "%LOCALAPPDATA%\programs\python\python38-32\lib\site-packages\pgzero\data;pgzero\data" ^
--add-data "images;images" ^
--add-data "music;music" ^
--add-data "sounds;sounds" ^
--add-data "icon.png;." ^
"Around The Way.py"
```
