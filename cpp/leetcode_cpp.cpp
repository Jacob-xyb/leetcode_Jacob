#include <iostream>
#include "Jx_test.h"
using namespace std;


int main()
{
    vector<int> a{ 1,2,2,1 };
    //cout << singleNumber_Jx002(a) << endl;
    unordered_set<int> s1(a.begin(), a.end());
    for (unordered_set<int>::const_iterator p = s1.begin(); p!= s1.end(); p++)
    {
        cout << *p << " ";
    }
    system("pause");
    return 0;
}