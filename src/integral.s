# segment danych -----------------------------------------
.section .data
koniec_przedzialu: .float 100.0
dwa: .float 2.0
liczba_prostokatow: .long 0
szerokosc_prostokata: .float 0.0
wynik: .float 0.0
temp: .float 0.0

# segment tekstu (kodu) ----------------------------------
.section .text
.globl integral
integral:
    movl 4(%esp), %eax              /* argument ze stosu (liczba prostokatow) do eax */
    mov %eax, liczba_prostokatow    /* liczba prostokatow do odpowiedniego miejsca w pamieci */
    finit                           /* inicjalizacja koprocesora */
    movl liczba_prostokatow, %ecx   /* liczba prostokatow do licznika */
    fildl liczba_prostokatow        /* liczba prostokatow ST(0) */
    fld koniec_przedzialu           /* liczba prostokatow w ST(1) ostatnia liczba ST(0) */
    fdivp                           /* szerokosc prostokata teraz w ST(0) */
    fst szerokosc_prostokata        /* szerokosc do pamieci i zostaje na stosie,
                                       jest to pierwsze miejsce z ktorego bedziemy liczyc wartosc */

petla:
    fst temp                        /* do temp miejsce nowego prostokata */
    fmul temp                       /* wyliczenie wartosci x^2 */
    fsub dwa                        /* odjecie 2, daje to wartosc x^2 - 2 */
    fadd wynik                      /* dodanie dotychczasowej sumy do wysokosci obecnego prostokata */
    fstp wynik                      /* zapisz zsumowany wynik w pamieci i zdejmij ze stosu */
    decl %ecx                       /* dekrementacja licznika prostokatow */
    cmpl $0, %ecx                   /* sprawdzenie czy są jeszcze prostokaty */
    je koniec                       /* jesli nie to wyjdz */
    fld temp                        /* na wierzcholek stosu miejsce ostatniego prostokata */
    fadd szerokosc_prostokata       /* oblicz miejsce kolejnego prostokatu */
jmp petla                           /* bedzie sie wykonywalo dopoki sa prostokaty */

koniec:
    fld wynik                       /* wynik na szczycie stosu */
    fmul szerokosc_prostokata       /* wynik * szerokosc prostokata i to na szczycie stosu */
    ret                             /* najwyzsza wartosc na stosie jest wartoscia zwracana przez funkcje */
