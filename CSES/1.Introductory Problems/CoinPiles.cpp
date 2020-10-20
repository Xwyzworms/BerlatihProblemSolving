#include <iostream>
using namespace std;


#define ll long long

int main()
{

int t =0;

cin>>t;

while(t)
{
	int x,y;
	cin>>x>>y;
	
	if(x*y % 3 == 0)
	{
		cout<<"YES";
	}
	else
	{
		cout<<"NO";
	}
		
	
	t--;
	
}	
	
	
}
