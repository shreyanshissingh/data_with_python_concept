## OOP Concepts: Revision Notes

This folder contains practical Python code and notes to help you understand and revise Object-Oriented Programming (OOP) concepts. Below are the main OOP concepts, each explained in simple language with 2-3 line definitions for easy revision.

### 1. Class & Object
- **Class:** A class is like a blueprint or template for creating objects. It defines what properties and behaviors the objects will have. For example, a `Car` class can describe what all cars have in common, like wheels and the ability to drive.
- **Object:** An object is an actual instance created from a class. It represents a real thing you can work with in your code, like a specific car made using the `Car` class blueprint. Each object can have its own unique values for the properties defined in the class.

### 2. Constructor
- **Constructor:** A constructor is a special method in a class that gets called automatically when you create a new object. It is used to set up the object with initial values or perform any setup steps needed. In Python, the constructor method is called `__init__`.

### 3. Encapsulation
- **Encapsulation:** Encapsulation means keeping the internal details of how an object works hidden from the outside world. You interact with the object using its public methods, without needing to know how everything is done inside. This helps protect the data and makes the code easier to use and maintain.

### 4. Data Extraction
- **Data Extraction:** Data extraction is about getting information out of objects, usually through methods or properties. It allows you to access the data stored inside an object in a controlled way, ensuring that only the right information is shared and used.

### 5. Class Methods
- **Class Methods:** Class methods are functions that belong to the class itself, not to any one object. They can be used to perform actions that affect the whole class or to create objects in special ways. In Python, you use the `@classmethod` decorator and pass `cls` as the first argument.

### 6. Inheritance
- **Inheritance:** Inheritance lets you create a new class based on an existing class. The new class (child) automatically gets the features and behaviors of the old class (parent), but you can also add new features or change how things work. This helps you reuse code and build more complex systems easily.

### 7. Polymorphism
- **Polymorphism:** Polymorphism means using the same method name for different types of objects, and each object can have its own way of doing things. For example, both `Dog` and `Cat` classes can have a `speak()` method, but each will make a different sound. This makes your code more flexible and easier to extend.

### 8. Decorators
- **Decorators:** Decorators are special functions that can change or add to the behavior of other functions or methods. They are often used to add extra features like logging, access control, or timing, without changing the original code. In Python, decorators use the `@` symbol before the function name.

### 9. Multithreading
- **Multithreading:** Multithreading allows your program to run multiple tasks at the same time, making it faster and more efficient, especially when dealing with tasks that can happen independently. It is useful for speeding up programs that need to do many things at once, like downloading files or handling user input.

### 10. Pydantic
- **Pydantic:** Pydantic is a Python library that helps you define and validate data using Python type hints. It makes sure your data is correct and structured, which is especially useful when working with APIs or user input. Pydantic models are easy to use and help catch errors early.

### 11. Async
- **Async:** Async programming lets your code do other things while waiting for slow operations, like reading files or fetching data from the internet. This makes your programs more responsive and efficient, as they don't get stuck waiting for one thing to finish before starting another.

---
Refer to the code in each chapter for practical examples and deeper understanding of these concepts.
