#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h> 

FILE *fp, *f1, *f2;
const int STR_L = 128;
char str[STR_L];
typedef long double Double;

const size_t sizeDict = 3000;
const size_t sizeDoc = 30;

struct DICT {
       	char dict[sizeDict][STR_L];  // 300 is an arbitrary boundary
        Double idf[sizeDict];
        int n; // actual size
};

struct DOC {
	char doc[sizeDict][STR_L]; // 30 is set arbitrarily
        Double vec[sizeDoc];
        int n; // actual size
};

DICT readfileDic(const char *dictpathname, const char *tf_idfpathname){
    struct DICT dict;
    char str[128];
    Double val;
    size_t nb = 0, nt = 0;
    fp=fopen(dictpathname,"r");
    if (fp != NULL){
    	while (fgets(str, sizeof(str), fp)){
            strcpy(dict.dict[nb++], str);
    	}
    }
    fclose(fp);
    fp=fopen(tf_idfpathname,"r");
    if (fp != NULL){
    	while (fgets(str, sizeof(str), fp)){
            if( 1==sscanf(str,"%Lf",&val)) {
                dict.idf[nt++] = val;
            }
    	}
    }
    fclose(fp);
    if (nb == nt)
    {dict.n = nb;}
    else
    {printf("realfileDic::diction. and tfidf are not of the same size"); exit(0);}
    return dict;
}

DOC readfileDoc(const char *filepathname){
    struct DOC doc;
    size_t nb = 0;	
    fp=fopen(filepathname,"r");
    if (fp != NULL){
    	while (fgets(str, sizeof(str), fp)){
            strcpy(doc.doc[nb++], str);
    	}
    }
    doc.n = nb;
    fclose(fp);
    return doc; 
}

Double dicindoc(DOC *doc, const char *str){
    Double cnt = 0; 
    for(int i = 0; i < doc->n; ++i){
        if (strncmp (doc->doc[i], str, STR_L) == 0){
            cnt += 1.;
    }    }
    return (Double)cnt; 
}

//vectorise the doc against the dictionary coordinates and 
//reweight with the idf adjustement.
void vectorisationtfidf(const DICT *dict,DOC *doc){
    Double vecNorm = 0.;
    for (int i = 0; i < dict->n; ++i){
        doc->vec[i] = dicindoc(doc,dict->dict[i])*dict->idf[i];
        vecNorm += doc->vec[i]*doc->vec[i];
    }
    for (int i = 0; i < dict->n; ++i){
        doc->vec[i] = doc->vec[i]/vecNorm;
    }
}

Double sim_tfidf(const DICT *dict,DOC *doc1, DOC *doc2){ 
    Double sim = 0.;
    //vectorisation done with idf vector adjustement
    vectorisationtfidf(dict, doc1);
    vectorisationtfidf(dict, doc2);
    for (int i = 0; i < dict->n; i++){
        sim += doc1->vec[i]*doc2->vec[i];
    }
    return sim;
}

int main(int argc,char **argv) {
    char dictPathName[128] = "TOY/dict";
    char tfidfPathName[128] = "TOY/tf_idf";    
    if(argc != 3){	
        printf("!!!expected input: <program> doc1 doc2"); 
	exit (EXIT_FAILURE);
    }

    DICT dict = readfileDic(dictPathName,tfidfPathName);
    DOC doc1 = readfileDoc(argv[1]);
    DOC doc2 = readfileDoc(argv[2]);

//compute similarity
printf("%Lf \n",sim_tfidf(&dict,&doc1,&doc2));

} 
