#include <iostream>
using namespace std; 


int arr[55];

int main(){
    int max = 0;
    int min = 0;
    int length;
    int multiple;

    cin >> length;

    for (int i = 0; i < length; i ++){
        cin >> arr[i];
    }

    max = arr[0];
    min = arr[0];

    for (int i = 0; i < length; i ++){
        if(max < arr[i]){
            max = arr[i];
        }
        else if (min > arr[i]){
            min = arr[i];
        }
    }
    cout << max * min; 

    return 0;
}
