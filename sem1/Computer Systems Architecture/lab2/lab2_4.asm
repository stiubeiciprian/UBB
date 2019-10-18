;Write a program in the assembly language that computes the following arithmetic expression, considering the given data types for the variables.
; a,b,c - byte, d - word
; [2*(a+b)-5*c]*(d-3)
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
    b db 4
    c db 2
    d dw 12


segment code use32 class=code
    start:
        
        
        xor eax, eax
        xor ebx, ebx
        xor edx, edx
        
        ;5*c
        mov al, 5   ; AL = 5
        mul byte [c]; AX = AL * [c] = 10
        
        mov dx, ax ; DX = AX
        
        ; 2*(a+b)
        mov bl, [a] ; BL = [a] = 2
        add bl, [b] ; BL = BL + [b] = 2 + 4 = 6
        
        mov al, 2   ; AL = 2
        
        mul byte bl ; AX = AL * BL = 2 * 6 = 12
        
        ;2*(a+b)-5*c
        sub ax, dx ; AX = AX - DX = 12 - 10 = 2
        
        ; d-3
        mov dx, [d] ; DX = [d] = 12
        
        sub dx, 3 ; DX = DX - 3 = 12 - 3 = 9
        
        ;[]*()
        
        mul word dx ; DX:AX = AX * DX = 2 * 9 = 18
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
