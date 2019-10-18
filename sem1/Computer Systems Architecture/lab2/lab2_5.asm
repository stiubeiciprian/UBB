;Write a program in the assembly language that computes the following arithmetic expression, considering the given data types for the variables.
; a,b,c,d-byte, e,f,g,h-word
; (a*b)/c
; ex1:(4*3)/2 = 12 / 2 = 6
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 4
    b db 3
    c db 2


segment code use32 class=code
    start:
        
        xor eax, eax
        
        mov al, [a] ; AL = [a] = 4
        mul byte [b] ; AX = AL * [b] = 4 * 3 = 12
        div byte [c] ; AL = AX / [c] =  12 / 2 = 6
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
