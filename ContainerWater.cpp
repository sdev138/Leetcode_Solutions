#include <iostream>
#include <algorithm> 
#include <cmath>
#include <vector> 

int maxArea(std::vector<int>); 
int main(int argc, char** argv) {
  // pushing the values into the vector 
  std::vector<int> height; // adding 9 elements 
  height.push_back(1); 
  height.push_back(8); 
  height.push_back(6); 
  height.push_back(2); 
  height.push_back(5);
  height.push_back(4); 
  height.push_back(8); 
  height.push_back(3); 
  height.push_back(7); 

  
  std::cout << "Entering the function" << std::endl; 
  int finalValue = maxArea(height); // getting the maximum value of the function 

  std::cout << "The max area of the vector is: " << finalValue << std::endl;
  return 0; 
}

// must be less than O(n^2)
int maxArea(std::vector<int> height) {
  std::cout << "Beginning of the function" << std::endl;
  int maxArea = 0; 
  int left = 0; // left side of the vector 
  int right = height.size() - 1; // right side of the vector 

  // while the left pointer is to the right of the right pointer 
  while (left < right) {
    int standardHeight = std::min(height[left], height[right]); // taking the min value between height[left] and height[right]

    if ((standardHeight * (right - left)) > maxArea) {
      maxArea = standardHeight * (right - left); 
    }

    if (height[right] > height[left]) {
      left++;
    } else {
      right--;
    }
  }

  return maxArea; 
}
