/*The ticket booking system of Cinemax theater has to be implemented using C++ program. There are
10 rows and 7 seats in each row. Doubly circular linked list has to be maintained to keep track of free
seats at rows. Assume some random booking to start with. Use array to store pointers (Head
pointer) to each row. On demand
a) The list of available seats is to be displayed
b) The seats are to be booked
c) The booking can be cancelled
CODE:
*/

#include <iostream>
#include <stdlib.h>
using namespace std;
class Node {
public:
 Node* next;
 Node* prev;
 int seat;
 string id;
 int status;
};
class Cinemax {
public:
 Node* head, * tail, * temp;
 Cinemax() {
 head = NULL;
 }
 void create_list();
 void display();
 void book();
 void cancel();
 void avail();
};
void Cinemax::create_list() {
 int i = 1;
 temp = new Node;
 temp->seat = 1;
 temp->status = 0;
 temp->id = "null";
 tail = head = temp;
 for (int i = 2; i <= 70; i++) {
 Node* p = new Node;
 p->seat = i;
 p->status = 0;
 p->id = "null";
 tail->next = p;
 p->prev = tail;
 tail = p;
 tail->next = head;
 head->prev = tail;
 }
}
void Cinemax::display() {
 int r = 1;
 temp = head;
 int count = 0;
 cout << "\n---------------------------------------------------------------\n";
 cout << " Screen this way \n";
 cout << "---------------------------------------------------------------\n";
 while (temp->next != head) {
 cout << "S" << (temp->seat < 10 ? "0" : "") << temp->seat << " :";
 if (temp->status == 0)
 cout << "|___| ";
 else
 cout << "|_B_| ";
 count++;
 if (count % 7 == 0) {
 cout << endl;
 r++;
 }
 temp = temp->next;
 }
 cout << "S" << (temp->seat < 10 ? "0" : "") << temp->seat << " :";
 if (temp->status == 0)
 cout << "|___| ";
 else
 cout << "|_B_| ";
}
void Cinemax::book() {
 int x;
 string y;
label:
 cout << "\n\nEnter seat number to be booked: ";
 cin >> x;
 cout << "Enter your ID number: ";
 cin >> y;
 if (x < 1 || x > 70) {
 cout << "Enter a correct seat number to book (1-70)\n";
 goto label;
 }
 temp = head;
 while (temp->seat != x) {
 temp = temp->next;
 }
 if (temp->status == 1)
 cout << "Seat already booked!\n";
 else {
 temp->status = 1;
 temp->id = y;
 cout << "Seat " << x << " booked!\n";
 }
}
void Cinemax::cancel() {
 int x;
 string y;
label1:
 cout << "Enter seat number to cancel booking: ";
 cin >> x;
 cout << "Enter your ID: ";
 cin >> y;
 if (x < 1 || x > 70) {
 cout << "Enter a correct seat number to cancel (1-70)\n";
 goto label1;
 }
 temp = head;
 while (temp->seat != x) {
 temp = temp->next;
 }
 if (temp->status == 0) {
 cout << "Seat not booked yet!\n";
 } else {
 if (temp->id == y) {
 temp->status = 0;
 cout << "Seat Cancelled!\n";
 } else {
 cout << "Wrong User ID! Seat cannot be cancelled!\n";
 }
 }
}
void Cinemax::avail() {
 temp = head;
 int count = 0;
 cout << "\n\n\n";
 cout << "---------------------------------------------------------------\n";
 cout << " Screen this way \n";
 cout << "---------------------------------------------------------------\n";
 while (temp->next != head) {
 if (temp->status == 0) {
 cout << "S" << (temp->seat < 10 ? "0" : "") << temp->seat << " :";
 cout << "|___| ";
 count++;
 if (count % 7 == 0) {
 cout << endl;
 }
 }
 temp = temp->next;
 }
 if (temp->status == 0) {
 cout << "S" << (temp->seat < 10 ? "0" : "") << temp->seat << " :";
 cout << "|___| ";
 }
}
int main() {
 Cinemax obj;
 obj.create_list();
 int ch;
 char c = 'y';
 while (c == 'y') {
 obj.display();
 cout << "\n*********************************************\n";
 cout << " CINEMAX MOVIE THEATRE\n";
 cout << "*********************************************\n";
 cout << "\nEnter Choice:\n1. Current Seat Status\n2. Book Seat\n3. Available Seats\n4. Cancel Seat\n";
 cin >> ch;
 switch (ch) {
 case 1:
 obj.display();
 break;
 case 2:
 obj.book();
 break;
 case 3:
 obj.avail();
 break;
 case 4:
 obj.cancel();
 break;
 default:
 cout << "Wrong choice input!\n";
 }
 cout << "\nDo you want to perform any other operation? (y/n)\n";
 cin >> c;
 }
 return 0;
}