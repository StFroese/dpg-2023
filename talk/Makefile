all: download_images build/talk.pdf

texoptions = \
	     --lualatex \
	     --interaction=nonstopmode \
	     --halt-on-error \
	     --output-directory=build

plots: build/plots/reco_0.pdf

build/plots/reco_0.pdf: plots/plot_reco.py | build/plots
	python $< $@ $(DATA)

build/talk.pdf: plots FORCE | build
	latexmk $(texoptions) talk.tex

download_images: build/images/telescope_render.jpg

build/images/telescope_render.jpg: build/images
	curl -o $@ https://live.staticflickr.com/65535/30329828142_122b021818_o_d.jpg

build/images:
	mkdir -p build/images

build/plots:
	mkdir -p build/plots

preview: FORCE | build
	latexmk $(texoptions) -pvc talk.tex

FORCE:

build:
	mkdir -p build

clean:
	rm -r build
