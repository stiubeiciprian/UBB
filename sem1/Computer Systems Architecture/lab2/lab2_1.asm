;Write a program in the assembly language that computes the following arithmetic expression, considering the given data types for the variables.
;Compute and analyze the result:
;256*1
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...

; our code starts here
segment code use32 class=code
    start:
       ; 256*1
        
        xor eax, eax
        xor ebx, ebx
        
        mov ax, 256 ; AX = 256
        
        mov bx, 1 ; BX = 1
        
        mul bx ; DX:AX = AX *  BX = 256 * 1 = 256
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
