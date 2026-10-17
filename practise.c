#include<stdio.h>
// int main(){
//     int a ;
//     printf("enter grades = ");
//     scanf("%d" , &a);
//     if (a<30){
//         printf("C grade");
//     } else if (a>=30 && a<70){
//         printf("B grade");
//     } else if (a>=70 && a<90){
//         printf("A grade");
//     } else if (a>=90 && a<100){
//         printf("A+ grade");
//     } else{
//         printf("invalid grade");
//     }
//     return 0;
// }



// int main(){
//     char ch;
//     printf("enter character = ");
//     scanf("%c" , &ch);
//     if (ch >= 'A' && ch <= 'Z'){
//         printf("uppercase letter");
//     } else if (ch >= 'a' && ch <= 'z'){
//         printf("lowercase letter");
//     } else if (ch >= '0' && ch <= '9'){
//         printf("digit");
//     } else{
//         printf("special character");
//     }
    
//     return 0;
// }



// int main(){
//      int a ;
//      printf("enter a number = ");
//      scanf("%d", &a);
//      for (int i = 0 ; i<=a ; i++){
//         printf("%d \n" , i);
//      }
//     return 0;
// } 



// int main(){
//     int a ;
//     printf("enter a number = ");
//     scanf("%d" , &a);
//     int i = 0;
//     while (i <= a){
//         printf("%d" , i );
//         i++;
//     }
//     return 0;
// }



//  int main(){
//      int a ;
//      printf("enter a number = ");
//      scanf("%d" , &a);
//      for (int i=10 ; i >= 1 ; i-- ){
//          printf("%d x %d = %d \n" , a , i , a*i);
//      }
//      return 0;
//  }



// int main(){
//     int a ;
//     int b = 1;
//     printf("enter a number = ");
//     scanf("%d" , &a);
//     for (int i = 1 ; i<=a ; i++){
//         b *= i;
//     printf("factorial of %d is %d \n" , a , b);    
//     }
//     return 0;
// }



// void hello();
// void goodbye();

// void hello(){
//     printf("hello \n");
// }
// void goodbye(){
//     printf("goodbye \n");
// }

// int main(){
//     hello();
//     goodbye();
//     return 0;
// }



// void namaste();
// void bonjour();

// void namaste(){
//     printf("namaste \n");
// }
// void bonjour(){
//     printf("bonjour \n");
// }
// int main(){
//     printf("enter f for french and i for indian = ");
//     char ch ;
//     scanf("%c" , &ch);
//     if (ch == 'f'){
//         bonjour();
//     } else if (ch == 'i'){
//         namaste();
//     } else{
//         printf("invalid entry");
//     }
//     return 0;
// }



void square();
void circle();
void rectangle();

void square(){
    int a;
    printf("enter lenght of side of square = ");
    scanf("%d" , &a);
    printf("area of square = %d" , a*a);
}
void circle(){
    int r;
    printf("enter radius of circle = ");
    scanf("%d" , &r);
    printf("area of circle = %f" , 3.14*r*r);
}
void rectangle(){
    int l , b;
    printf("enter length and breadth of rectangle = ");
    scanf("%d %d" , &l , &b);
    printf("area of rectangle = %d" , l*b);
}
int main(){
    printf("enter s for square , c for circle and r for rectangle = ");
    char ch ;
    scanf("%c" , &ch);
    if (ch == 's'){
        square();
    } else if (ch == 'c'){
        circle();
    } else if (ch == 'r'){
        rectangle();
    } else{
        printf("invalid entry");
    }
    return 0; 
}  