#include <iostream>

using namespace std;
int main()
{
	int inp;
	cin >> inp;
	int prev =0;
	long long answer =0 ; 
	
	for (int i =0 ; i < inp ; i++)
	{
		int inp2;
		cin >>inp2;
		if (prev > inp2) 
		{
			answer = answer + (prev - inp2); //# steps required.
			
		}
		else
		{
			prev = inp2;
			
		}

}
cout<<answer;
}
