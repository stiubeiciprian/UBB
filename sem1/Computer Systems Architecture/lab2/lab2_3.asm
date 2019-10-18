;Write a program in the assembly language that computes the following arithmetic expression, considering the given data types for the variables.
; a,b,c,d - word
; c - (d+a) + (b+c)
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    
    a dw 4
    b dw 2
    c dw 10
    d dw 3
    

; our code starts here
segment code use32 class=code
    start:
        
        xor eax, eax
        xor ebx, ebx
    
        mov ax, [c] ; AX = [c] = 10
        mov bx, [d] ; BX = [d] = 3
        
        add bx, [a] ; BX = BX + [a] = 3 + 4 = 7
        sub ax, bx  ; AX = AX - BX = 10 - 7 = 3
        
        mov bx, [b] ; BX = [b] = 2
        
        add bx, [c] ; BX = BX + [c] = 12
        
        add ax, bx  ; AX = AX + BX = 3 + 12 = 15
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
