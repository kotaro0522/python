#include <iostream>

using namespace std;

int main() {
  int n;
  int arr[400000][400000] = {};
  int temp;
  int max_length = 1;
  int current_position = 0;
  cin >> n;
  cin >> temp;
  arr[0][0] = temp;
  for(int i = 0; i< n-1; i++){
    cin >> temp;
    for(int j = 0; j<n; j++){
      for(int k = 0; k<n; k++){
        if(arr[j][k]==0){
          if(arr[j][k-1] == temp-1){
            arr[j][k] = temp;
          }
          if(k+1>max_length){
            max_length = k+1;
          }
          temp = 0;
          break;
        }
      }
      if(temp == 0){
        break;
      }
    }
    if(temp != 0){
      arr[current_position+1][0] = temp;
      current_position++;
    }
  }
  cout << arr << endl;
}
