FSHARPCOMPILER:=/usr/bin/fsharpc

TARGET:=analysisRUN.exe
FILES:=utils.fs vectors.fs matrices.fs myIO.fs analysis.fs
TARGETS:=utils.exe vectors.exe matrices.exe myIO.exe analysis.exe
FLAGS:= --checked- --optimize+

all: 
	$(FSHARPCOMPILER) --out:$(TARGET)  $(FILES)
	@echo $(TARGET) "was built"

test:	@echo -n 'No Testing yet!'

clean:
		rm -f $(TARGETS)
