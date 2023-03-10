all: download_images build/talk.pdf

texoptions = \
	     --lualatex \
	     --interaction=nonstopmode \
	     --halt-on-error \
	     --output-directory=build

build/talk.pdf: FORCE | build
	latexmk $(texoptions) talk.tex

download_images: build/images/telescope_render.jpg

build/images/telescope_render.jpg: build/images
	curl -o $@ https://live.staticflickr.com/65535/30329828142_122b021818_o_d.jpg

build/images:
	mkdir -p build/images

preview: FORCE | build
	latexmk $(texoptions) -pvc talk.tex

FORCE:

build:
	mkdir -p build

clean:
	rm -r build
