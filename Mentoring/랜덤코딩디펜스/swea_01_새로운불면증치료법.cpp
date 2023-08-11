#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, N, cnt, sum;
    cin >> T;;
    for (int i= 1; i < T+1; ++i){
        int arr[10] = {false}; 
        cin >> N;
        cnt = 0;
        while (true) {
            cnt++;
            string str = to_string(N*cnt);
            for (int j = 0; j < str.length(); j++) {
                int tmp = str[j] - '0';
                arr[tmp] = true;
            }
            sum = 0;
            for (int j = 0; j < 10; j++) {
                if (arr[j] == true) {
                    sum += 1;
                }
            }
            if (sum == 10) {
                cout << '#' << i << ' ' << cnt*N << endl;;
                break;
            }
        }
        
        
    }

    return 0;
}