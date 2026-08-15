
main:
	pyinstaller --onefile --hidden-import=unicodedata --add-data 'templates:templates' --add-data 'static:static' frontend.py

windows:
	python -m PyInstaller --onefile --hidden-import=unicodedata --hidden-import=Flask --add-data 'templates;templates' --add-data 'static;static' frontend.py

