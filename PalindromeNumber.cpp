#include <iostream>
#include <vector>

class Solution {
  public:

  // empty constructor 
  Solution() {}

  bool isPalindrome(int x) {
    std::vector<int> pali; 

    if (x == 0) {
      return true; 
    }

    // checking if the number is a single digit 
    if (x/10 == 0) {
      return true;
    }

    int originalNum = x; 
    double reversedNum = 0; 

    while (x != 0) {
      int digit = x % 10; 
      reversedNum = (reversedNum * 10) + digit; 

      x /= 10; // decreasing the value of the number 
    }

    return originalNum == reversedNum; 
  }
};

int main(int argc, char** argv) {
  int num = 1001; 
  Solution *solution = new Solution();   

  bool test = solution->isPalindrome(num);

  if (test == true) {
    std::cout << "The number: " << num << " is a palindrome" << std::endl;
  } else {
    std::cout << "The number: " << num << " is not a palindrome" << std::endl;
  } 

  return 0; 
}