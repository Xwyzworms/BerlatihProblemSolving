#include <iostream>

using namespace std;

int main()
{
string inp;
char DNA = 'A';
int c = 0 ,answer = 0 ;
cin >>inp;

for (char s : inp)
{
	if (s == DNA )
	{
		c++;
		answer = max(c , answer);
	}
	else
	{
		DNA = s; // Change the DNA
		c = 1;  // Well Sure it's 1 right?
		
		
	}
	
	
}
	
cout<<answer;	
	
}

