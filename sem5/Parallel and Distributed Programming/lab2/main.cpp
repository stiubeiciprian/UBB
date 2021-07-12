#include <iostream>
#include <vector>
#include <queue>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <assert.h>

using namespace std;

const int VECTOR_SIZE = 100000;

mutex mu;
condition_variable cv;

queue<int> q;
int sum = 0;

int generateRandomNumber() {
    return rand() % 100;
}

/**
 * Computes the product of each element in a and b, storing the results in q.
 */
void producer(vector<int> a, vector<int> b, int vectorSize) {
    for (int i = 0; i < vectorSize; ++i) {
        lock_guard<mutex> lg(mu);
        q.push(a[i] * b[i]);
        cv.notify_one();
    }
}

/**
 * Computes the sum of values in q.
 */
void consumer(int vectorSize) {
    for (int i = 0; i < vectorSize; ++i) {
        unique_lock<mutex> ul(mu);
        cv.wait(ul, [] { return !q.empty(); });
        sum = sum + q.front();
        q.pop();
    }
}

void printVector(vector<int> v) {
    for (int a : v) {
        cout<< a << " ";
    }
    cout << endl;
}

void producer_consumer() {
    vector<int> v1(VECTOR_SIZE);
    vector<int> v2(VECTOR_SIZE);

    srand(time(nullptr)); // use current time as seed

    // Initialize v1 and v2 with random numbers.
    generate(v1.begin(), v1.end(), generateRandomNumber);
    generate(v2.begin(), v2.end(), generateRandomNumber);

//    printVector(v1);
//    printVector(v2);

    double duration;
    clock_t start = clock();

    thread t2(consumer, VECTOR_SIZE);
    thread t1(producer, v1, v2, VECTOR_SIZE);
    t1.join();
    t2.join();

    duration = ( clock() - start );
    cout << "Operation took "<< duration << "ms" << endl;
    cout<< "sum = " << sum;

}

void producer_consumer_test(vector<int> a, vector<int> b, int vectorSize, int expectedSum) {
    thread t2(consumer, vectorSize);
    thread t1(producer, a, b, vectorSize);
    t1.join();
    t2.join();

    assert(sum == expectedSum);
    sum = 0;
}

void test() {
    vector<int> a = {1,2,3};
    vector<int> b = {1,2,3};
    producer_consumer_test(a,b,3,14);


    vector<int> c = {1,2,3,4};
    vector<int> d = {21,30,40,12};
    producer_consumer_test(c,d,4,249);
}

int main() {
    test();
    producer_consumer();

    return 0;
}
