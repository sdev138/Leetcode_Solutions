#include <iostream>

class Node {
  public:
  Node *next; 
  int val; 

  // empty constructor
  Node() {}
  Node(int value) {
    val = value; 
  }
  
};

int main(int argc, char** argv) {
  std::cout << "Beginning of the function" << std::endl; 

  
  return 0; 
}