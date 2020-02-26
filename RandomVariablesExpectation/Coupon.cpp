/*
Vázquez Choreño Luis Ernesto
Randomized Algorithms
Application: Example Coupon Collectors Problem



g++ -std=c++11 Coupon.cpp  && ./a.out

*/

#include <bits/stdc++.h>

using namespace std;
typedef long long lli;



int get_rng(int value){ return (rand()%value ) + 1;}

int randomized_algorithm(int num_coupons){
  vector<bool> collector(num_coupons + 5,false);
  int counter = 0;
  int iteration = 0;
  while(counter < num_coupons){
    iteration++;
    int rng = get_rng(num_coupons);
    if(collector[rng] == true){
      continue;
    }else{
      collector[rng] = true;
      counter++;
    }
  }
  return iteration;
}






int main(){
  srand(time(NULL));
  int num_coupons = 100;
  cout << "Expected value: "  << ((double)(num_coupons) * log(num_coupons) + num_coupons) << "\n";
  cout << "Practice: " << randomized_algorithm(num_coupons) << "\n";

  vector<int> x;
  vector<double> expected_y;
  vector<double> practice_y;

  for(int i=1;i<=num_coupons;i+=5){
    x.push_back(i);
    expected_y.push_back( i * log(i) + i);
    practice_y.push_back(randomized_algorithm(i));
  }


}
