FSHARPCOMPILER:=/usr/bin/fsharpc

TARGET:=analysisRUN.exe
FILES:=utils.fs vectors.fs matrices.fs analysis.fs
TARGETS:=utils.exe vectors.exe matrices.exe analysis.exe


all: 
	$(FSHARPCOMPILER) --out:$(TARGET) --checked- --optimize+ $(FILES)
	@echo $(TARGET) "was built"

test:	@echo -n 'No Testing yet!'

clean:
		rm -f $(TARGETS)
