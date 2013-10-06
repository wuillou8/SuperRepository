#include <iostream>  

#include <sstream>  

    

using namespace std;  

    

struct Item {  
    string name, type, color, hand;  
};  


bool parse(istream &, Item &);  

bool parse(const string &, Item &);  

void print(const Item &);  

void test(istream &);    

int main() {  

     stringstream ss;  

     ss << "name1#type1#color1#hand1\n" 
         << "name2#type2#color2#hand2#\n" 
         << "name3#type3#color3\n" 
         << "foo";  

     test(ss);  

     return 0;  

}  

    
void test(istream &in) {  

     string line;  
     while(getline(in, line)) {  
         Item item;  
         cout << line << endl;  

         if (parse(line, item)) {  

             print(item);  

         } else {  

             cout << "FAIL" << endl;  

         }  

     }  

 }  

    

    

void print(const Item &item) {   

     cout << "Item('" << item.name  

         << "','" << item.type  

         << "','" << item.color  

         << "','" << item.hand   

         << "')" << endl;  

}  

    

bool parse(istream &in, Item &item) {  

     if (!getline(in, item.name, '#')) { return false; }  

     if (!getline(in, item.type, '#')) { return false; }  

     if (!getline(in, item.color, '#')) { return false; }  

     if (!getline(in, item.hand, '#')) { return false; }  

     return true;  

}  

    

bool parse(const string &s, Item &item) {  

     istringstream stream(s);  

     return parse(stream, item);  

} 



