/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;
// 100 0 
int main() {
    int T, len;
    cin >> T;
    for (int t = 1; t < T+1; t++) {
        string cheifs;
        cin >> cheifs;
        int *counts = new int[16];
        
        for (int i = 0; i < 16; i++) counts[i] = 0;
        
        counts[1]++; // A가 열쇠를 갖고있다.

        for (int i = 0; i < cheifs.length(); i++) {
            int *newCnts = new int[16];
            for (int j = 0; j < 16; j++) newCnts[j] = 0;
            
            int cheif = cheifs[i] - 'A';

            for (int j = 0; j < 16; j++) {
                if(!(j & 1 << cheif)) continue;
                
                long long cnt = 0;
                for(int k = 0; k < 16; k++) {
                    if(!(k & j)) continue;
                    
                    cnt += counts[k];
                    
                    cnt %= 1000000007;
                }
                
                newCnts[j] = cnt;
                
            }
            
            delete counts;
            counts = newCnts;
            
        }
        
        int sum = 0;
        for (int i = 0; i < 16; i++) {
            sum += counts[i];
            sum %= 1000000007;
        }
        
        delete counts;
        
        cout << '#' << t << ' ' << sum << endl;
    }
    return 0;
}

