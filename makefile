
main:
	pyinstaller --onefile --hidden-import=unicodedata --add-data 'templates:templates' --add-data 'static:static' frontend.py
