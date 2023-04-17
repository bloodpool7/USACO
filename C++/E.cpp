#include <bits/stdc++.h>

typedef long long ll;
using namespace std;


int main(){
    for (int x = 800; x <= 900; x++){
        ll count1 = 0;
        ll count2 = 0;
        ll count3 = 0;
        for (ll i = 1; i <= x; i++){
            for (ll j = 1; j <= x; j++){
                for (ll k = 1; k <= x; k++){
                    if ((i*i + j*j + k*k) <= x*x){
                        count1 ++;
                    }
                }
            }
        }
        for (ll i = 1; i <= x; i++){
            for (ll j = 1; j <=x; j++){
                if ((i * i) + (j*j) <= x*x){
                    count2 ++;
                }
            }
        }

        ll answer = 8 * count1 + 12 * count2 + 6 * x + 1;
        cout << answer << endl;
    }

    // int x;
    // cin >> x;
    // ll count1 = 0;
    // ll count2 = 0;
    // ll count3 = 0;
    // for (ll i = 1; i <= x; i++){
    //     for (ll j = 1; j <= x; j++){
    //         for (ll k = 1; k <= x; k++){
    //             if ((i*i + j*j + k*k) <= x*x){
    //                 count1 ++;
    //             }
    //         }
    //     }
    // }
    // for (ll i = 1; i <= x; i++){
    //     for (ll j = 1; j <=x; j++){
    //         if ((i * i) + (j*j) <= x*x){
    //             count2 ++;
    //         }
    //     }
    // }

    // ll answer = 8 * count1 + 12 * count2 + 6 * x + 1;
    // cout << answer << ", ";
}