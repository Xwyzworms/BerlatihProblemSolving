#include <iostream>

using namespace std;
int main()
{
long long n , answer = 0;
cin >> n;

for (int i = 1 ; i < n ;i++)
{
	int ans;
	cin >> ans;
	answer = answer + ans; // Sum Every Single input;
}
cout << n*(n+1)/2 - answer; // 5*(5+1)/2 = 15 then - answer ..





}


