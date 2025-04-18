/*Department of Computer Engineering has student's club named 'Pinnacle Club'. Students of second, third and final year of department can be granted membership on request. Similarly one may cancel the membership of club. First node is reserved for president of club and last node is reserved for secretary of club. Write C++ program to maintain club member‘s information using singly linked list. Store student PRN and Name. Write functions to: 
a) Add and delete the members as well as president or even secretary. 
b) Compute total number of members of club 
c) Display members 
d) Two linked lists exists for two divisions. Concatenate two lists.
*/

#include<iostream>
#include<stdlib.h>
using namespace std;
struct node
{
char prn[10];
char name[20];
node*next;
}*president,*secratory,*new1,*curr;
void creat_list()
{
int count,i;
cout<<"\n Enter total number of members in pinnacle list : ";
cin>>count;
for(i=0;i<(count-1);i++)
{
if(president==NULL && secratory==NULL)
{
president=new node;
cout<<"\n Enter PRN number of president : ";
cin>>president->prn;
cout<<"\n Enter name of the President : ";
cin>>president->name;
president->next=NULL;
curr=president;
secratory=new node;
cout<<"\n Enter PRN number of secreatory : ";
cin>>secratory->prn;
cout<<"\n Enter name of the Secratory : ";
cin>>secratory->name;
secratory->next=NULL;
}
else
{
new1=new node;
cout<<"\n Enter PRN number of the member : ";
cin>>new1->prn;
cout<<"\n Enter Name of the member : ";
cin>>new1->name;
curr->next=new1;
new1->next=secratory;
curr=new1;
}
}
}
void del_pr()
{
curr=president;
president=curr->next;
delete curr;
}
void del_sec(node *curr)
{
node *temp;
while((curr->next)->next!=NULL)
{
curr=curr->next;
}
temp=curr->next;
curr->next=NULL;
delete temp;
}
void display()
{
node *curr;
curr=president;
while(curr!=NULL)
{
cout<<curr->prn<<"-"<<curr->name<<"->";
curr=curr->next;
}
}
void countnodes()
{
int total;
total=0;
node *curr;
curr=president;
while(curr!=NULL)
{
total++;
curr=curr->next;
}
cout<<"\n Total number of members in CLUB : "<<total;
}
void reverse(node *curr)
{
if(curr->next==NULL)
{
cout<<curr->prn<<"-"<<curr->name<<"->";
}
else
{
reverse(curr->next);
cout<<curr->prn<<"-"<<curr->name<<"-";
}
}
void add_mem()
{
new1=new node;
cout<<"\n Enter PRN number of member : ";
cin>>new1->prn;
cout<<"\n Enter name of the member : ";
cin>>new1->name;
new1->next=secratory;
curr->next=new1;
curr=new1;
}
int main()
{
int ch;
do
{
cout<<"\n-----------MENU------------";
cout<<"\n 1. Create ";
cout<<"\n 2. Display ";
cout<<"\n 3. Add Member ";
cout<<"\n 4. Reverse ";
cout<<"\n 5. Delete President ";
cout<<"\n 6. Delete Secratory ";
cout<<"\n 7. Count Nodes ";
cout<<"\n 8. Exit ";
cout<<"\n Enter your Choice : ";
cin>>ch;
switch(ch)
{
case 1:creat_list();
break;
case 2:display();
break;
case 3:add_mem();
break;
case 4:reverse(president);
break;
case 5:del_sec(president);
break;
case 6:del_pr();
break;
case 7:countnodes();
break;
case 8:exit(0);
cout<<"\n Thank You for using the Program!!!!";
break;
default:cout<<"\n Invalid choice ";
}
}while(ch!=8);
}