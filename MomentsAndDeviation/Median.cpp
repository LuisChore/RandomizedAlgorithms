/*

Vázquez Choreño Luis Ernesto
Randomized Algorithms
Application: Median

g++ -std=c++11 Median.cpp  && ./a.out

*/

#include <bits/stdc++.h>
using namespace std;
const int inf_int = 10000;


int get_rng(int value){ return (rand()%value ) + 1;}

/// MEDIAN ALGORITHM
vector<int> generate_random_array(int n){
  vector<int> v(n);
  for(int i=0;i<n;i++){
    v[i] = get_rng(inf_int);
  }
  return v;
}


void process_agorithm_randomized(vector<int> &S){
  bool found = false;
  int n = S.size();
  while(found == false){
    int size_r = ceil(pow(n,0.75));
    vector<int> R(size_r);
    // first step
    for(int i=0;i<R.size();i++){
      R[i] = S[get_rng(n) - 1];
    }

    // second step
    sort(R.begin(),R.end());

    // third step
    int d = R[floor(size_r/2.00 - pow(n,0.5))];

    // fourth step
    int u = R[ ceil(size_r/2.00 + pow(n,0.5))];


    // fifth step
    vector<int> C;
    int ld = 0,lu = 0;
    for(int i=0;i<n;i++){
      if(d <= S[i] and S[i]<=u){
        C.push_back(S[i]);
      }else if(S[i] < d){
        ld++;
      }else{
        lu++;
      }
    }


    // sixth step
    if(ld > (n>>1) || lu > (n>>1))
      continue;

    // seventh step
    if(C.size() > 4*size_r)
      continue;
    sort(C.begin(),C.end());

    // eight step
    int median_index = (n>>1) - ld ;
    cout << "Median computed: " << C[median_index] << "\n";
    found = true;
  }
}




/// R-SELECT

int partition(vector<int> &S,int l,int r){
  int value = S[r];
  int i = l;
  for(int j = l; j < r; j++){
    if(S[j] <= value){
      swap(S[i],S[j]);
      i++;
    }
  }
  swap(S[i],S[r]);
  return i;
}


int r_select(vector<int> &S,int l,int r,int k){
  int len = r - l + 1;
  int pivot = get_rng(len) - 1 + l;
  swap(S[pivot],S[r]);
  int pos =  partition(S,l,r);
  if(pos - l == k)
    return S[pos];
  if(pos - l > k)
    return r_select(S,l,pos-1,k);
  return r_select(S,pos+1,r,k-pos+l-1);
}


void r_select(vector<int> &S){
  int len = S.size();
  int median = r_select(S,0,len-1,(len)>>1);
  cout << "Median computed: " << median << "\n";
}









int main(){

  srand(time(NULL));
  int n = 333;
  vector<int> random_array = generate_random_array(n);
  vector<int> copy_array(random_array);
  sort(copy_array.begin(),copy_array.end());
  cout << "Real median: " << copy_array[n>>1] << "\n";


  process_agorithm_randomized(random_array);
  r_select(random_array);

  return 0;
}
