/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
// Is Unique: Implement an algorithm to determine if 
// a string has all unique characters.


bool isUniqueString(std::string str){
    
        std::transform(str.begin(), str.end(), str.begin(), ::tolower);
        
        if(str.length() > 128) return false;
        int char_set[str.length()];
        for (int i=0;i<str.length();i++){
            int Ascii = str.at(i);
            if(char_set[Ascii] == Ascii ) {
                return false;
            }
            char_set[Ascii] = Ascii;
        }
        return true;
}
int main()
    
{
    std::string lol = "Sampi";
    std::cout<<isUniqueString(lol); // 0
    return 0;
}