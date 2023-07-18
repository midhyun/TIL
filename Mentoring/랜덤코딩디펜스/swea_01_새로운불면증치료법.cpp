#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, N, cnt, sum;
    cin >> T;;
    for (int i= 0; i < T; ++i){
        int arr[10] = {false}; 
        cin >> N;
        cnt = 0;
        while (true) {
            cnt++;
            string str = to_string(N*cnt);
            for (int j = 0; j < str1.length(); j++) {
                arr[stoi(str[j])] = true;
            }
            sum = 0;
            for (j = 0; j < 10; j++) {
                if (arr[i] == true) {
                    sum += 1;
                }
            }
            if (sum == 10) {
                cout << '#' << i << ' ' << cnt;;
                break
            }
        }
        cout << N << endl;
        
    }

    return 0;
}