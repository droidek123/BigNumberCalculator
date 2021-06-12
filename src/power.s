.section .data                       # część programu zawierająca dane zainicjalizowane
zaok_najblizszej: .short 0x03B       # wartość słowa kontrolnego odpowiedzialna za zaokrąglanie do najblizsza_wartosc
zaok_w_dol: .short 0x43B             # wartość słowa kontrolnego odpowiedzialna za zaokrąglanie w dół
zaok_w_gore: .short 0x83B            # wartość słowa kontrolnego odpowiedzialna za zaokrąglanie w górę
zaok_obcinanie: .short 0xC3B         # wartość słowa kontrolnego odpowiedzialna poprzez obcięcie
zero_val: .double 0x1
# formaty oraz łańcuchy do wypisań
.section .text
.globl power
power:

# prolog - nowa ramka stosu
push %ebp
movl %esp, %ebp

# laduj a do st(0)

mov 16(%ebp),%eax
mov 20(%ebp),%edx

cmp $1, %eax                    # zaokrąglenie zostało wybrane, w przypadku błednego
je najblizsza_wartosc             # wybrania dojdzie do skoku do etykiety inne, a
cmp $2, %eax                    # wypisania komunikatu, a następnie zakończenia programu
je w_dol
cmp $3, %eax
je w_gore
cmp $4, %eax
je obcinanie
jmp obcinanie
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
cmpl $0, %edx
je zero
cmpl $1, %edx
je jeden
jmp dwa
zero:
fldl zero_val
jmp koniec
jeden:
jmp koniec
dwa:
fldl 8(%ebp)
fldl 8(%ebp)
fmulp
dec %edx
dec %edx

potega:
cmpl $0, %edx
jz koniec
fldl 8(%ebp)
fmulp
dec %edx
jmp potega

# wynik w st(0)
# przywracamy stos
koniec:
mov %ebp, %esp
pop %ebp
# powrot
ret
