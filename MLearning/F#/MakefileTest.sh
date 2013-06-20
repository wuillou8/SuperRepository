FSHARPCOMPILER:=/usr/bin/fsharpc

TARGETS:=utils.exe vectors.exe matrices.exe analysis.exe

all:	$(TARGETS)

%.exe:	%.fs
	$(FSHARPCOMPILER) --checked- --optimize+ $^

#include ../Makefile.common

test:	@echo -n 'No Testing yet!'

clean:
		rm -f $(TARGETS)
