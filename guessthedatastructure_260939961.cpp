#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main() {
  int n;
  int inout, x;
  while (cin >> n) {

    bool isStack = true;
    bool isQueue = true;
    bool isPQueue = true;

    stack<int> s;
    queue<int> q;
    priority_queue<int> pq;
  
    for (int i = 0; i < n; i++) {
      cin >> inout >> x;
      if (inout == 1) {
        // Only input if isStack is still true
        if (isStack) s.push(x);
        // Only input if isQueue is still true
        if (isQueue) q.push(x);
        // Only input if isPQueue is still true
        if (isPQueue) pq.push(x);
      } 
      if (inout == 2) {
        if (isStack) {
        // Only take out element if stack is not empty and the top element = x
          if (!s.empty() && s.top()==x) {
            s.pop();
          } else {
            isStack = false;
          }
        }
        // Only take out element if queue is not empty and the front element = x
        if (isQueue) {
          if (!q.empty() && q.front()==x) {
            q.pop();
          } else {
            isQueue = false;          
          }
        }
        // Only take out element if priority queue is not empty and the top element = x
        if (isPQueue) {
          if (!pq.empty() && pq.top()==x) {
            pq.pop();
          } else {
            isPQueue = false;
          }
        }
      }
    }
    if (!isPQueue && !isStack && !isQueue) {
      cout << "impossible" << endl;
    } else if (isStack && !isQueue && !isPQueue) {
      cout << "stack" << endl;
    } else if (isQueue && !isStack && !isPQueue) {
      cout << "queue" << endl;
    } else if (isPQueue && !isStack && !isQueue) {
      cout << "priority queue" << endl;
    } else {
      cout << "not sure" << endl;
    }
  }

}
