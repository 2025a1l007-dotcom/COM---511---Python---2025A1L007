#include <iostream>
using namespace std;

class Student
{
public:
    string name;
    int rollno;

    void display()
    {
        cout << "Student Name: " << name << endl;
        cout << "Roll Number: " << rollno << endl;
    }
};

int main()
{
    Student s1;

    cout << "Enter student name: ";
    cin >> s1.name;

    cout << "Enter roll number: ";
    cin >> s1.rollno;

    s1.display();

    return 0;
}