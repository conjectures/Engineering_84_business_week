# Python: Object Oriented Programming

## What is OOP
Object Oriented Programming is one of the most widely used programming paradigms.
As the name implies, OOP works with objects.
In python these are also refered to as classes, and they are used to bind data or functionality in a simple structure.

## Four pillars
Object Oriented Programming is based on four core principles, also known as pillars of OOP: **Encapsulation**, **Abstraction**, **Inheritance** and **Polymorphism**.

- **Encapsulation**

**Encapsulation** is achieved when a class has an internal, *private* state, which is maintained by its own internal functions.
The user doesn't impact the class state directly, but can access it via the public functions, or methods that the class provides.
Encapsulation is a core pillar of OOP as it more generally models the way objects behave in real life.
To demonstrate this, consider a dog that has internal "private attributes" such as hunger, sleepiness and thirst.
The owner of the dog can't really control these attributes; instead he can perform certain functions to impact them indirectly. 
Specifically, the owner can fill the dog's bowl with food and water and provide a bed for his pet.

- **Abstraction**

**Abstraction** is an extension of encapsulation, which aims to simplify the usage of the classes by exposing only a high-level mechanism of using it.
That is, the class is developed in a way that the implementation details are hidden and only the relevant operations should be exposed to the user.
Most electronic appliances apply this concept in real life. A fridge or a lamp have very different purposes but they both require electricity to start working.
The user knows how to plug in the lamp and fridge to the mains electricity but he doesn't need to know how a heat pump works, or how LEDs use electroluminescence to shine.

- **Inheritance**

**Inheritance** is very useful when there are similar objects that share common functionality but are not entirely the same.
With inheritance, a class can pass down functionality to *children* classes, where the same code can be reused without rewriting the same methods.
These children classes can then add more specific functionality and pass those down to other children, thus, forming a hierarcy of *parent* and *child* classes.
A typical hierarchical inheritance example would be the class of *dogs*, which inherits from the class *mammals*, which in turn inherits from class *animals*

- **Polymorphism**

**Polymorphism** is a Greek word that means to take more than one form; 
Similarly, OOP classes should be able to take other forms, in the sense that an inherited class methods and attributes should be able to change according to the new object's needs.
This could be as simple as increasing the arguments of a methods, to overwriting the whole function.
An example of polymorphism could be found in the real life:
If an inherited trait of mammals is the fact that they give birth to live younglings, the platypus, which is also classified as a mammal, is the exception.
Instead, the platypus 'overwrites' this trait and changes it to laying eggs.

## Why use Object Oriented Progaramming?
The use of OOP is justified with many benefits.

### Code reuse
Firstly, from one of the four pillars of OOP, inheritance, a lot of code gets to be reused, saving a lot of time in development. 
Additionally, if for example we need to add or change a functionality in children classes of a single parent class; by applying the change to the parent class all of its inheritants will also be affected.
Thus, by this simple relation, a lot extra work can be avoided.

### Flexibility of code
Throught polymorphism, the objects can be reused and adapted, according to the use case. 
This means that, the same library can be used in many different projects and can be fine-tuned to work perfectly for each instance.
On many occasions, by using the same tried and tested code in different situations, can prove to be more time saving and less error prone, rather than rewriting the code from scratch

### Easier troubleshooting
OOP promotes the creation of small and modular code, which makes it easier to troubleshoot errors in case something goes wrong. 
Moreover, as promoted through encapsulation, additional functionality can be added to classes to handle errors, display messages or other helpful operations.

### Intuitive structure
Object-Oriented Programming is more in line to the way humans see and interact with the world.
Applying this higher-level approach to programming makes it easier to code and solve complicated problems.
Code can be split into small chunks that can be solved, one at a time;

