#include <stdio.h>
#include <stdlib.h>

double addition(double a, double b, int x);
double subbtract(double a, double b, int x);
double multiply(double a, double b, int x);
double divide(double a, double b, int x);
double integral(long a);
double power(double a, int x, int y);

double sqrtassemb(double a, int x);
double sinus(double a, int x);
double cosinus(double a, int x);

double add(double a, double b, int x){
  return addition(a,b,x);
}

double subb(double a, double b, int x){
  return subbtract(b,a,x);
}

double mul(double a, double b, int x){
  return multiply(a,b,x);
}

double divd(double a, double b, int x){
  return divide(b,a,x);
}

double inte(long a){
  return integral(a);
}

double powerto(double a, int x, int y){
  return power(a,x,y);
}


double square(double a, int x){
  return sqrtassemb(a, x);
}

double sinassemb(double a, int x){
  if((int)a % 360 == 0){
    return 0;
  }
  else if((int)a % 270 == 0){
    return -1;
  }
  if((int)a % 180 == 0){
    return 0;
  }
  else if((int)a % 90 == 0){
    return 1;
  }
  else return sinus(a,x);
}

double cosassemb(double a, int x){
  if((int)a % 360 == 0){
    return 1;
  }
  else if((int)a % 270 == 0){
    return 0;
  }
  else if((int)a % 180 == 0){
    return -1;
  }
  else if((int)a % 90 == 0){
    return 0;
  }
  else return cosinus(a, x);
}
