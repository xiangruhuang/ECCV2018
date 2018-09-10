all:
	python draw.py > mesh.pov
	povray mesh.pov
	xdg-open mesh.png
