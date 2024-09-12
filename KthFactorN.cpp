#include <iostream>
#include <vector>

class Solution {
  public:
    int kthFactor(int n, int k) {
        vector<int> factors; 
        int i = 1;
        while (i <= n) {
            if (n%i == 0) {
                factors.push_back(i);
            }
            i++; 
        }

        if (k > factors.size()) {
            return -1;
        } else {
            return factors[k-1]; 
        }
    }

    private:

    void findValue(int value) {
        return value
    }
};
