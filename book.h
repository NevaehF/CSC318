

// Messy starter Version 
/*
#pragma once
#include <iostream> 
#include <string>
using namespace std;

class bk {
public:
	bk() {}

	void t(string a) { ttl = a; } // title 
	void a(string b) { auth = b; } // author
	void p(string c) { pages = stoi(c); } // page number
	void sh() { cout << ttl << "," << auth << "." << pages << endl; } // print info
	
private: 
	string ttl; // title 
	string auth; // author 
	int pages; // number of pages 
};

*/


// Refactored/ Cleanup Version 


#pragma once
#include <iostream>
#include <string>
using namespace std;

// Class to store and display our book information
class book {
public:
	book() : pages(0) {}// our empty constructor 

	// This will set the title of the book 
	void setTitle(string t) { title = t; } 

	// This will set the author of our book 
	void setAuthor(string a) {author = a; }

	// This will set the number of pages {MUST BE POSITIVE} 
	void setNumberOfPages(int p) {
		if (p <= 0) {
			throw invalid_argument("Pages must be a greater number than 0");
		}
		pages = p; 
	}

	// Display all of the stored book information
	void displayInfo() const {
		cout << "Title: " << title
			<< "\nAuthor: " << author
			<< "\nNumber of Pages: " << pages << endl;
	}

private:
	string title; // Title of the book
	string author; // Author of the book
	int pages; // Number of pages in the book
};
