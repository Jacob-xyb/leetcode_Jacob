#include <iostream>
#include "Jx_test.h"
using namespace std;


int main()
{
    vector<int> a{ 2,7,11,15 };
    cout << twoSum_Jx001(a, 9)[0] << endl;
    cout << twoSum_Jx001(a, 9)[1] << endl;

    system("pause");
    return 0;
}