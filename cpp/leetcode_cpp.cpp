#include <iostream>
#include "Jx_test.h"
using namespace std;


int main()
{
    vector<int> a{ -2,1,-3,4,-1,2,1,-5,4 };
    cout << maxSubArray(a) << endl;

    system("pause");
    return 0;
}