#include <iostream>
#include <string>

class Solution {
public:
  int romanToInt(std::string s) {
    int solutionValue = 0;
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == 'I') {
        if (i + 1 < s.length()) {
          if (s[i + 1] == 'V') {
            i++;
            solutionValue += 4;
          } else if (s[i + 1] == 'X') {
            i++;
            solutionValue += 9;
          } else {
            solutionValue += 1;
          }
        } else {
          solutionValue += 1;
        }
      } else if (s[i] == 'X') {
        if (i + 1 < s.length()) {
          if (s[i + 1] == 'L') {
            i++;
            solutionValue += 40;
          } else if (s[i + 1] == 'C') {
            i++;
            solutionValue += 90;
          } else {
            solutionValue += 10;
          }
        } else {
          solutionValue += 10;
        }
      } else if (s[i] == 'C') {
        if (i + 1 < s.length()) {
          if (s[i + 1] == 'D') {
            i++;
            solutionValue += 400;
          } else if (s[i + 1] == 'M') {
            i++;
            solutionValue += 900;
          } else {
            solutionValue += 100;
          }
        } else {
          solutionValue += 100;
        }
      } else if (s[i] == 'V') {
        solutionValue += 5;
      } else if (s[i] == 'L') {
        solutionValue += 50;
      } else if (s[i] == 'D') {
        solutionValue += 500;
      } else if (s[i] == 'M') {
        solutionValue += 1000;
      }
      std::cout << "Value of solutionValue: " << solutionValue << std::endl;
    }
    return solutionValue;
  }
};
