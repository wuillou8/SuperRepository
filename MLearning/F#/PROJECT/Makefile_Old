all: utils.exe vectors.exe matrices.exe analysis.exe 
	 
utils.exe: Utils.fs
	fsharpc --nologo --out:utils.exe Utils.fs

vectors.exe: Vectors.fs Utils.fs 
	fsharpc --nologo --out:vectors.exe Utils.fs Vectors.fs
		 
matrices.exe: Matrices.fs Vectors.fs Utils.fs
	fsharpc --nologo --out:matrices.exe Utils.fs Vectors.fs Matrices.fs

analysis.exe: Analysis.fs Matrices.fs Vectors.fs Utils.fs
	fsharpc --nologo --out:analysis.exe Utils.fs Vectors.fs Matrices.fs Analysis.fs

clean:
		-rm *.exe
