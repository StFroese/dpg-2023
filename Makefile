all: talk/build/talk.pdf

talk/build/talk.pdf: FORCE
	make -C talk

FORCE:

.phony: all FORCE
