.section .data                       # część programu zawierająca dane zainicjalizowane
zaok_najblizszej: .short 0x03F       # wartość słowa kontrolnego odpowiedzialna za zaokrąglanie do najblizsza_wartosc
zaok_w_dol: .short 0x43F             # wartość słowa kontrolnego odpowiedzialna za zaokrąglanie w dół
zaok_w_gore: .short 0x83F            # wartość słowa kontrolnego odpowiedzialna za zaokrąglanie w górę
zaok_obcinanie: .short 0xC3F         # wartość słowa kontrolnego odpowiedzialna poprzez obcięcie
# formaty oraz łańcuchy do wypisań
.section .text
.globl divide
divide:

# prolog - nowa ramka stosu
push %ebp
movl %esp, %ebp

# laduj a do st(0)
fldl 8(%ebp)
# laduj b do st(0), w st(1) jest b
fldl 16(%ebp)
# dodaj st(0) + st(1) -> st(0)

mov 24(%ebp),%eax
cmp $1, %eax                    # zaokrąglenie zostało wybrane, w przypadku błednego
je najblizsza_wartosc             # wybrania dojdzie do skoku do etykiety inne, a
cmp $2, %eax                    # wypisania komunikatu, a następnie zakończenia programu
je w_dol
cmp $3, %eax
je w_gore
cmp $4, %eax
je obcinanie

w_dol:              # ustawnienie zaokrąglenia w dół
fldcw zaok_w_dol
jmp dzialanie

w_gore:             # ustawnienie zaokrąglenia w górę
fldcw zaok_w_gore
jmp dzialanie

obcinanie:          # ustawnienie zaokrąglenia w przez obcięcie
fldcw zaok_obcinanie
jmp dzialanie

najblizsza_wartosc: # ustawnienie zaokrąglenia do najbliższej wartości
fldcw zaok_najblizszej

dzialanie:

fdivp
# wynik w st(0)
# przywracamy stos
mov %ebp, %esp
pop %ebp
# powrot
ret
