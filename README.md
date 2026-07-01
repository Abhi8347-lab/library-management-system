 Library Management System

A fully object-oriented Python project that models how a 
real library works — built to demonstrate all four pillars 
of OOP in one working system.

 What it does?

- Members can borrow and return books
- Librarians can add and remove books from the library
- Tracks available copies — can't borrow what isn't there
- Search books by author across the entire collection

 Concepts used

- **Encapsulation** — book copy count is private, 
  only changes through validated methods
- **Inheritance** — Member and Librarian both extend 
  a base Person class
- **Polymorphism** — same method call, different 
  behavior depending on role
- **Abstraction** — Person defines the contract, 
  subclasses implement it

 What's coming next?

- Save/load library data from a JSON file
- Exception handling for edge cases
- SQL database backend
- REST API with FastAPI

 Built by

Abhiram deevi— learning Python and AIML, 
documenting every step on GitHub.
