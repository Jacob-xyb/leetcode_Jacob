#include "../Jx_test.h"

//time:4 ms	//memory:6 MB	//rank:59.39%
//写的很心累 各种问题
int reverse_Jx001(int x)
{
    {
        string s = to_string(abs(x));
        int n = s.size();
        for (int i = 0; i < n / 2; i++)
        {
            char temp = s[i];
            s[i] = s[n - i - 1];
            s[n - i - 1] = temp;
        }
        int res = atoi(s.c_str());
        if (x < 0) { res = -res; }
        if (atof(s.c_str()) < -pow(2, 31) || atof(s.c_str()) > pow(2, 31) - 1)
        {
            return 0;
        }
        return res;
    }
}

int reverse_Eg001(int x)
{
    int min = -1 * pow(2, 31);
    int max = pow(2, 31) - 1;
    long int temp;
    long int res = 0;
    if (x > max || x < min)
    {
        return 0;
    }

    while (x != 0)
    {
        temp = x % 10;
        x = x / 10;
        res = res * 10 + temp;
    }
    if (res > max || res < min)
    {
        return 0;
    }
    return res;
}

int reverse_Eg002(int x)
{
    int rev = 0;
    while (x != 0) {
        if (rev < INT_MIN / 10 || rev > INT_MAX / 10) {
            return 0;
        }
        int digit = x % 10;
        x /= 10;
        rev = rev * 10 + digit;
    }
    return rev;
}