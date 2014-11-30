#include<stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *fp, *f1, *f2;
const int STR_L = 128;
char str[STR_L];

struct DOC {
	char doc[30][STR_L];
        int n;	
};

DOC readfileDoc(char* filepathname){
    struct DOC doc;
    fp=fopen(filepathname,"r");
    size_t nb = 0;
    if (fp != NULL){
    	while (fgets(str, sizeof(str), fp)){
            strcpy(doc.doc[nb++], str);
    	}
    }
    doc.n = nb;
    fclose(fp);
    return doc; 
}

double sim_00(DOC doc1, DOC doc2){
    double sim = 0.;
    int numb = 0;
    for(int i = 0; i < doc1.n; i++){
        for(int j = 0; j < doc2.n; j++){
            if(strncmp (doc1.doc[i], doc2.doc[j], 128) == 0 ){
	        numb += 1;
	    }
	}
    }
    if( doc1.n < doc1.n )
    {return (double)numb/doc1.n;}
    else 
    {return (double)numb/doc2.n;}
}

int main(int argc,char **argv) {

    if(argc != 3)
    {	
        printf("!!!expected input: <program> doc1 doc2"); 
	exit (EXIT_FAILURE);
    }

    DOC mydoc1 = readfileDoc(argv[1]);
    DOC mydoc2 = readfileDoc(argv[2]);

printf("sim: %f ",sim_00(mydoc1,mydoc2));
} 
