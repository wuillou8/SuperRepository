rm -f tmp.tex tmp.ps  tmp.dvi $1.ps  $1.png
gnuplot $1
latex tmp.tex
dvips -o tmp.ps tmp.dvi
mv tmp.dvi $1.dvi
mv tmp.ps $1.ps
ps2pdf $1.ps
rm tmp*
