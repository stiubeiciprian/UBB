; Given the words A and B, compute the doubleword C as follows:
; the bits 0-2 of C are the same as the bits 12-14 of A
; the bits 3-8 of C are the same as the bits 0-5 of B
; the bits 9-15 of C are the same as the bits 3-9 of A
; the bits 16-31 of C are the same as the bits of A

; a = 1111 1111 1111 1111 
; b = 0000 0000 0000 0000
; c = 1111 1111 1111 1111 1111 1110 0000 0111 = FFFFFE07h
bits 32

global start
   
extern exit
import exit msvcrt.dll

segment data use32 class=data
    a dw 0FFFFh
    b dw 0000h
    c dd 0

segment code use32 class=code
    start:
        ; bits 16-31
        mov eax, [c] ; eax = [c] = 0000h
        mov ax, [a] ; ax = [a] = 1111h
        shl eax, 16 ; shift 16 bits to the left ( high part of eax <- ax , ax <- 0 )
        
        ;bits 9-15
        mov bx, [a] ; bx = [a] = 0FFFFh
        and bx, 0000001111111000b ; isolate bits 3-9 of A
        mov cl, 6
        rol bx, cl ; rotate 6 positions to the left
        or ax, bx ; put the bits in result
        
        ;bits 3-8
        mov bx, [b] ; bx = [b] = 0000h
        and bx, 0000000000111111b ; isolate bits 0-5 of B
        mov cl, 3
        ror bx, cl ; rotate 3 positions to the right
        or ax, bx ; put the bits in result
        
        ;bits 0-2
        mov bx, [a] ; bx = [a] = 0FFFFh
        and bx, 0111000000000000b ; isolate bits 12-14 of A
        mov cl, 12
        ror bx, cl ; rotate 12 positions to the right
        or ax, bx ; put the bits in the result
        
        mov [c], ax ; put the result in memory 
        
        
        
        
        
        push    dword 0
        call    [exit]
