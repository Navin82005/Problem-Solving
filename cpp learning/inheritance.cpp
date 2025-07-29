#include <iostream>
using namespace std;

// class Animal
// {
//     public:
//     virtual void makeSound() {
//         std::cout << "This is a Animal Sound";
//     }
// };


// class Dog : public Animal
// {
//     public:
//     void makeSound() override
//     {
//         std::cout << "Bow Bow";
//     }
// };

// class Cat : public Animal
// {
//     public:
//     void makeSound() override
//     {
//         std::cout << "Meow Meow";
//     }
// };

// int main()
// {
//     Animal ani;
//     ani.makeSound();
// }

class Base {
public:
    virtual void show() {
        std::cout << "Base class show" << std::endl;
    }
};

class Derived : public Base {
public:
    void show()
    {
        std::cout << "Derived class show" << std::endl;
    }
};

int main() {
    Base* ptr = new Derived();
    //  new Base();
    // ptr->show(); // Calls Base::show - static binding
    
    int x = 5;
    int& ref = x;

    cout << &x << " " << &ref;
    // cout << ptr;
    // ptr->show(); // Calls Base::show - static binding, because the pointer type is Base*

    delete ptr;
    return 0;
}
