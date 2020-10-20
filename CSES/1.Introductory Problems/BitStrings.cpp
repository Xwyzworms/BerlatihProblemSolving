# include<iostream>
# include<cmath>
using namespace std;

int main()
{
long long n = 0 , ans = 1;

cin>>n;


for(int i=0;i<n;i++)
{

ans = 2 * ans;
ans = ans % (long long)(1e9 + 7);
}
cout<<ans;

}

