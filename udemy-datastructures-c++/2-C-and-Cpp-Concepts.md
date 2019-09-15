1. Arrays
2. Structure
3. Pointers
4. Reference
5. Parameter Passing
6. Classes
7. Constructor
8. Templates

# Arrays
```
int main() {
    int A[5];
    int B[5] = {2, 4, 6, 8, 10};
    int i;
    for (i = 0; i < 5; i ++) {
        printf("%d", B[i]);
    }
}
```

Main Memory
------
Heap
------
Stack
------
Main

    A[5] B[2][4][6][8][10]
------
Code Section

    main() {
        blahblah
    }
------

# Structures
1. Defining Structure
2. Size of Structure
3. Declaring a structure
4. Accessing Members

E.x. Rectangle:
w * h

```
struct Rectangle
{
    int w;  // ----  2
    int h;  // ----  2
            //       4 bytes
}

int main() 
{
    struct Rectangle r; // 4 bytes , declaration
    r.h = 15
    r.w = 10

    -- or --
    struct Rectangle r = {10, 5}; // declaration + initialization

    printf("Area of rectangle is %d", r.w * r.h)
}
```

Main Memory
------
Heap
------
Stack
------
Main

    r[w][h]
------
Code Section

    main
    blahblah
------

## Examples of Struct:
1. Complex Number
a + ib

```
struct Complex 
{
    int real; // 2 bytes
    int img;  // 2 bytes
    // Total 4 bytes
};


```

2. Student
```
struct Student 
{
    int roll; // 2 bytes
    char name[25]; // 25 bytes
    char dept[10]; // 10 bytes
    char address[50]; // 50 bytes
    // Total 77 bytes
}

struct Student s;
s.roll = 10;
s.name = 'John';
...

```

3. Card

Face Value - 1, 2, ... 10, J, Q, K
Shape - 0(Clover), 1(Spade), 2(Diamond), 3(Heart)
Color - 0(Black), 1 (Red)
```
struct Card
{
    int face;  // 2 bytes
    int shape; // 2 bytes
    int color; // 2 bytes
               // 6 bytes
}

int main()
{
    struct Card c;
    c.face = 1
    c.shape = 0;
    c.color = 0;

    or 

    struct Card c = {1, 0 , 0};
}

----

int main() 
{
    struct Card deck[52]; // 52 * 6 = 312 bytes

    printf("%d", deck[0].face);
    printf("%d", deck[0].shape);
}
```

# Pointers
indirectly access data
- useful for accessing resources outside the program (e.g. heap memory)
1. accessing heap memory
2. accessing resources
3. parameter passing

```
a   <--- p
10       200

data variable: int a = 0;
address variable: int *p; //declaration
p = &a; //initialization
printf("%d", a); // 10
printf("%d", *p); // 10 (dereferencing)
```

```
#include <stdlib.h>
int main() {
    int *p;
    // in C:
    p = (int *) malloc(5 * sizeof(int))
    // in C++:
    p = new int[5];
}
```

# Reference
alias to variable (another name to a variable)

useful for parameter passing

```
int main() 
{
    int a = 10;
    int &r = a;
    cout << a; -- 10
    r ++;
    cout << r; -- 11
    cout << a; -- 11
}
```

# Pointer to structure

```
struct Rectangle
{
    int w;
    int h;
}

int main() 
{
    struct Rectangle r = {10, 5};
    struct Rectangle *p = &r;

    r.w = 15
    (*p).w = 20;
    p->w = 20;

    p = (struct Rectangle *) malloc (sizeof(struct Rectangle));
}
```