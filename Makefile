DATA := $(CURDIR)/data

all: talk/build/talk.pdf

talk/build/talk.pdf: FORCE
	make -C talk DATA=$(DATA)

clean:
	make -C talk clean

FORCE:

.phony: all FORCE
