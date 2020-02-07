/*
Vázquez Choreño Luis Ernesto
Randomized Algorithms
Application: Verifying Polynomial Identities



g++ -std=c++11 PolynomialIdentity.cpp  && ./a.out

*/




#include <bits/stdc++.h>

using namespace std;
typedef long long lli;


lli evaluate_product_form(vector<lli> &product_form,lli value);
lli evaluate_canonical_form(vector<lli> &canonical_form, lli value);
int get_rng(int value){ return (rand()%value ) + 1;}



// the chance that returns a wrong answer is no more than 1/n
bool randomized_algorithm(vector<lli> &product_form, vector<lli> &canonical_form,int degree){
  const int n = 100;
  // choose a number between [1,n*degree]
  int rng = get_rng(n*degree);
  // evaluate polynomials
  return (evaluate_product_form(product_form,rng) == evaluate_canonical_form(canonical_form,rng));
}



int main(){
  srand(time(NULL));
  /// (x + 1)(x − 2)(x + 3)(x − 4)(x + 5)(x − 6)
  vector<lli> product_form = {1,-2,3,-4,5,-6};
  // x^6 − 7x^3 + 25
  vector<lli> canonical_form = {1,0,0,-7,0,0,25};


  // //  (x + 1)(x + 2)
  // vector<lli> product_form = {1,2};
  // // x^2 + 3x + 2
  // vector<lli> canonical_form = {1,3,2};



  /// repeating the algorithm with replacement k times
  bool same = true;
  int k = 10;
  while(k--)
    same = same && randomized_algorithm(product_form,canonical_form,canonical_form.size() - 1);

  if(same)
    cout << "Same polynomials" << "\n";
  else
    cout << "Different polynomials" << "\n";


  return 0;
}







lli evaluate_product_form(vector<lli> &product_form,lli value){
  lli answer = 1LL;
  for(auto &u: product_form){
    answer = (answer * (value + u));
  }
  return answer;
}






lli evaluate_canonical_form(vector<lli> &canonical_form, lli value){
  lli answer = 0LL;
  reverse(canonical_form.begin(),canonical_form.end());
  lli v = 1LL;
  for(auto &u: canonical_form){
    answer = answer + v * u;
    v = value * v;
  }

  reverse(canonical_form.begin(),canonical_form.end());
  return answer;
}
