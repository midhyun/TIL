/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;
// 100 0 
int main()
{
    int N, M, T;
    cin >> T;
    for (int i = 1; i < T+1; i++) {
        bool flag = true;
        cin >> N;
        cin >> M;
        cout << "#" << i << " ";;
        for (int i = 0; i < N; i++) {
            int temp = (M >> i) & 1;
            if (!temp) {
                flag = false;
                cout << "OFF" << endl;;
                break;
            }
        }
        if (flag) {
            cout << "ON" << endl;;
        }
        
    }

    return 0;
}
