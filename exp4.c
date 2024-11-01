#include <stdio.h>
int q[10];
int rear=-1;
int front=-1;
int n;
void enqueue();
void dequeue();
void display();
int main() {
printf("enter the size of queue:");
scanf("%d",&n);
int choice;
do{
printf("enter the choice 1:enqueue 2:dequeue 3:peek 4:display 5:exit  ");
scanf("%d",&choice);
switch(choice)
{
case 1:
enqueue();
break;
case 2:
dequeue();
break;
case 3:
printf("peek element of stack %d:",q[front]);
case 4:
display();
break;
case 5:
printf("existing  ");
break;
default:
printf("invalid choice");
}
}
while(choice !=5);
}
void enqueue(){
if (rear>=n-1){
printf("q is full");}
else
{
if(front==-1){
front++;
}
rear++;

printf("enter the data to be entered \n");
scanf("%d",&q[rear]);
}
}
void dequeue()
{
if(front>rear){
printf("list is empty\n");}
else{
printf("deleted elements is %d \n",q[front]);
front++;
}}
void display(){
int i;
if(front>rear||front==-1){
printf("list is empty");
}
else{
for(i=front;i<=rear;i++){
printf("%d",q[i]);
}
}
}

