# include<iostream>
# include<cmath>
using namespace std;

#define ll long long
int main()
{
ll inp = 0;
ll ans =0;
cin>> inp;

for (ll i = 5 ; i<=inp ; i= i *5)
{
		
	ans = ans + inp/i; // Try to take a look at each factorial to get sense
	
}
cout<<ans;
	
}
