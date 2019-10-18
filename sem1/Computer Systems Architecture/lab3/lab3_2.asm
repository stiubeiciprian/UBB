;Write a program in assembly language which computes one of the following arithmetic expressions, considering the following domains for the variables (in the unsigned and signed representation).
;a - byte, b - word, c - double word, d - qword - Signed representation
;a + b + c + d - (a + b)
bits 32

global start
   
extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 2
    b dw -1
    c dd -3
    d dq 4
segment code use32 class=code
    start:
        
        mov al, [a] ; AL = [a] = 2
        cbw ; AX <- AL = 2
        
        add ax, [b] ; AX = AX + [b] = 2 + (-1) = 1
        
        cwde ; EAX <- AX = 1
        
        push eax ; (a+b) on stack = 1
        
        add eax, [c] ; EAX = EAX + [c] = 1 + (-3) = -2
        
        cdq ; EDX:EAX <- EAX = -2
        
        pop ebx ; EBX = a+b
        
        add eax, ebx ; EAX = EAX + EBX = -2 + 1 = -1
        adc edx, 0   ; add potential carry bit
        
        
        
        
    
        
        push    dword 0
        call    [exit]
