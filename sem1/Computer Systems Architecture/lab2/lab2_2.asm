;Write a program in the assembly language that computes the following arithmetic expression, considering the given data types for the variables.
; a,b,c,d - byte
;(a+b)-(a+d)+(c-a)
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    
    a db 2
    b db 1
    c db 20
    d db 3
    
segment code use32 class=code
    start:
        
        xor eax, eax
        xor ebx, ebx
        
        ; a + b 
        mov al, [b] ; AL = [b] = 1
        add al, [a] ; AL = AL + [a] = 1 + 2 = 3
        
        ; a + d
        mov bl, [d] ; BL = [d] = 3
        add bl, [a] ; BL = BL + [a] 3 + 2 = 5
        
        ; (a+b) - (a+d)
        sub al, bl ; AL = AL - BL  = 3 - 5 = -2
        
        ; c - a
        mov bl, [c] ; BL = [c] = 20
        sub bl, [a] ; BL = BL - [a] = 20 - 2 = 18
        
       ;(a+b)-(a+d)+(c-a)
        add eax, ebx ; EAX = EAX + EBX = -2 + 18 = 16
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
