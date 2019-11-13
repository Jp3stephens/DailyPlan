#include <iostream> 
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>

using namespace std; 

class  vectorClass { 
    //arr is the integer pointer which stores the address of 
    int* arr; 
    // capacity is the total storage capacity of the vector
    int capacity; 
    // current is the number of elements currently present in the vector
    int current; 

    public: 
        // Initial capacity of 1 element and allocating storage using dynamic allocation

        vectorClass(){ 
            arr = new int[1]; 
            capacity = 1;
            current = 0; 
        }

        void push(int data)
        { 
            // if num of elements equal to capacity, we don't have space to store more elements. So we double capacity
            if (current == capacity){ 
                int* temp = new int[2 * capacity]; 
                // copying old array elements to new array
                for (int i = 0; i < capacity; i++){ 
                    temp[i] = arr[i]; 
                }
                // delete previous array
                delete[] arr; 
                capacity *= 2; 
                arr = temp; 
            }
            // inserting data 
            arr[current] = data; 
            current++; 
        }

        // function to add element at any index
        void push(int data, int index)
        { 
            // if index is equal to capacity then this function is same as push function defined above
            if (index == capacity){ 
                push(data); 
            }
            else {
                arr[index] = data; 
            }
        }
        // function to extract element at any index
        int get(int index) { 
            // if index is within range
            if (index < current)
                return arr[index]; 
            return -1; 
        }
        // function to delete last element
        void pop() { 
            current--; 
        }
        // function to get the size of the vector
        int size(){ 
            return current; 
        }
        int getCapacity() { 
            return capacity; 
        }
        void print() { 
            for (int i = 0; i < current; i++){ 
                cout << arr[i] << " "; 
            }
            cout << endl; 

        }
}; 

int main()
{ 
    vectorClass v; 
    v.push(10); 
    v.push(20); 
    v.push(22); 
    v.push(3); 
    v.push(5); 
    v.push(100); 

    cout << "Vector size: "
    << v.size() << endl; 

    cout << "Vector capacity: " << v.getCapacity() << endl; 

    cout << "\n After updating 1st index" << endl; 
    cout << "Vector elements"; v.print(); 
    v.push(100, 1); 
    cout << "Element at 1st index : " << v.get(1) << endl; 
    v.pop(); 
    cout << "\nAfter deleting last element"
    << endl; 
    cout << "Vector size: " << v.size() << endl; 
    cout << "Vector capacity: " << v.getCapacity() << endl; 
    cout << "Vector elements : "; 
    v.print(); 
    return 0; 
}
