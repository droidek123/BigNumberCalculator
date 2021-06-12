all: main

main: main.c addition.s subbtract.s multiply.s divide.s integral.s sinus.s cosinus.s squareroot.s power.s 
gcc −shared−fPIC operations.c addition.s subbtract.s multiply.s divide.s integral.s sinus.s cosinus.s squareroot.s power.s −o operations.so

clean:
	rm main
