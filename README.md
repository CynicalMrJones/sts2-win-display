> [!WARNING]
> This is a work in progress
# Win lister
![image](https://github.com/CynicalMrJones/sts2-win-display/blob/master/sts2_wins.png)

# About
This project aims to display winning decks that are built in Slay the Spire 2. It uses 
flask and python to run a local server where you can see them in a browser.
## Methodology
I wanted to get better with web technologies so I chose flask with python to display data.
I usually don't reach for python but I have experience with JSON parsing using it. I needed
a JSON file because Slay the Spire 2 stores runs in .run files which are JSONS in disguies.
This is still a work in progress and will be updated for future beta branches.

# How to use

# Windows 
## Release page
1) Download sts2-win.exe under the Releases section
[RELEASES](https://github.com/CynicalMrJones/sts2-win-display/releases)
2) Run the executable 
3) Open a browser and connect to 127.0.0.1:5000
- localhost:5000 also works

# Linux
## Option 1 (Run with Python)
1) Clone repo
```
git clone https://www.github.com/cynicalmrjones/sts2-win-display
```
2) Install dependencies
```  
pip install flask 
```
3) Execute frontend.py
```
python3 frontend.py
```
4) Open a browser and connect to 127.0.0.1:5000
- localhost:5000 also works

## Option 2 (Release page)
1) Download sts_win_display under the Releases section
[RELEASES](https://github.com/CynicalMrJones/sts2-win-display/releases)
2) Run from terminal 
```
./sts_win_display
```
3) Open a browser and connect to 127.0.0.1:5000
- localhost:5000 also works

# Future Work
- Multiplayer support
- Relic display
- Enchant and upgrade display
- UI improvements
- Sorting
- Most won with card
- Least won with card
- General Optimizations
