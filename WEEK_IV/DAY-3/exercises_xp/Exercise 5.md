# The correct answer is option 2:

    class Labrador extends Dog {
      constructor(name, size) {
        super(name);
        this.size = size;
      }
    };


# Explanation:

When you extend a class with extends, you must call super() before using this in the constructor.

super(name) calls the parent class Dog constructor with the name argument.

Then you can safely assign this.size = size.

Why the others fail:

Option 1 → == This is used before calling super(). This causes a ReferenceError.==

Option 3 → == name is not defined in the constructor parameters, so super(name) fails.==

Option 4 → ==this.name = name is used before calling super(), which is illegal in derived classes.===
