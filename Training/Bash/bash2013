
#!/bin/bash 
# General script running dicts for a given INTEX dir: 
# the script runs the dicts and generates the Isr files, 
# load the corresponding files from INTEXdir into data, 
# then the path are changed back so that the sdostest files can be tested. 
# the cygwin path can be given and is translated into the dos path 

if [ "$1" = "" -o "$2" = "" ] 
then 
        echo "args in terminal: #1 file(s) #2 INTEXDIR" 
        echo $0 AUSRMBSBBSWTesting "\"I:\"" 
        exit 1 
else 
        # Initialisation Files/Path 
        echo "---*-File(s) treated: " `ls ${1}* | grep sdos` 
        intexdir=`cygpath.exe -d "${2}"\\\\` 
        echo "---*-INTEXDir: " \"${intexdir}\\\" 

fi 

# load scripts 
cp ../SCRIPT/scriptChgIsrDir.sh . 
cp ../SCRIPT/scriptChgIntexDir.sh . 
cp ../SCRIPT/scriptRunsdosfile.sh . 
cp ../SCRIPT/scriptCDUcdiIntoData.sh . 
cp ../SCRIPT/scriptChgIntexDir_data.sh . 

# treat only file named *sdos* 
for var in `ls -d "${1}"* | grep sdos` 
        do 
                ./scriptChgIsrDir.sh $var "..\IsrFiles" #"C:\RiskToolkit\pyTests\INTEX_NEW\IsrFiles" 
                ./scriptChgIntexDir.sh $var ${intexdir}\\ 
                ./scriptRunsdosfile.sh $var 
                ./scriptCDUcdiIntoData.sh  $intexdir 
                ./scriptChgIntexDir_data.sh $var 
        done 
./scriptChgIntexDir_data.sh ${intexdir} 

#del scripts 
rm scriptChgIsrDir.sh scriptChgIntexDir.sh scriptRunsdosfile.sh scriptCDUcdiIntoData.sh scriptChgIntexDir_data.sh 



-------------------------------------------- 

#!/bin/bash 
# Script locally copying the cdu/cdi files into the cmo_cdu/cmo_cdi files 
# The script creates local cmo_cdu/cdi directories in which the cdu/cdi files are copied 
if [ "$1" = "" ] 
then 
        echo "DOS IntexDir not specified as argument!" 
        echo "Into the terminal, enter the path (between apostrophes):" 
        echo $0 '"I:"' 
        exit 1 
else 
        intexdir=`cygpath.exe "$1"` 
        echo "---*-IntexDir: " $intexdir 
fi 


# Select out the isr files lines related to the cdu/cdi files. 
grep cmo_cdu isr* | grep OPEN > tmp_cdu 
grep cmo_cdi isr* | grep OPEN > tmp_cdi 
# creating the local cmo_cdu/cdi directories 
echo "---*-Creating cmo_cdu/cdi directories" 
mkdir cmo_cdu; mkdir cmo_cdi 
# Generate a copy of the relevant cmo_cdu subdirectory 
sed 's|.*cmo_cd[i-u]||;s|\\[^\]*$||;s|\\||;s|^|cmo_cdu/|;s|===$||' tmp_cdu | uniq | xargs -n1 mkdir -p 
# Copy the files from the cmo_cdu/cdi directories 
echo "---*-Copying the cmo_cdi files:" 
sed 's|.*cmo_cdi||;s|\\||g;s|===$||;s|^|/cmo_cdi\/&|' tmp_cdi | uniq | xargs -n1 -i cp "${intexdir}"{} "".{} 
echo "---*-Copying the cmo_cdu files:" 
# copy the files 
sed 's|.*cmo_cdu||;s|\\|\/|g;s|===$||;s|^|/cmo_cdu\/&|' tmp_cdu | uniq | xargs -n1 -i cp "${intexdir}"{} "."{} 
rm tmp_cdu, tmp_cdi 

