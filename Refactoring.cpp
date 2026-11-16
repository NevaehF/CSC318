// Refactoring.cpp : This file contains the 'main' function. Program execution begins and ends there.

/* Module 6 Assignment: Code Refactoring and Cleanup
	Nevaeh Fernandez
	08.20.2026
	CSC318
	nevferna@uat.edu
*/

/*
//Messy Starter Version 

#include "book.h" // make sure book.h in the same folder 

int main() {
	bk b;
	b.t("The Iliad");
	b.a("\nTranslated by: Emily Wilson");
	b.p("\n400");
	b.sh(); // prints all 
	return 0;
}


*/


// Refactored/ Cleanup Version 

#include "book.h" // links to header file that contains the class definition for our book class

int main() {
	try {
		book myBook;

		// This will set the book information 
		myBook.setTitle("Uzimaki");
		myBook.setAuthor("Junji Ito");
		myBook.setNumberOfPages(200);

		// This will display/print my book information
		myBook.displayInfo();
	}
	catch (const exception& e) {
		cout << "Error: " << e.what() << endl; 
	}

	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
