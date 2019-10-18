;Write a program in assembly language which computes one of the following arithmetic expressions, considering the following domains for the variables (in the unsigned and signed representation).
;a - byte, b - word, c - double word, d - qword - Unsigned representation
;((a + a) + (b + b) + (c + c)) - d

bits 32

global start
   
extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 1
    b dw 2
    c dd 3
    d dq 12
    
segment code use32 class=code
    start:
        
        xor eax,eax
        xor edx,edx
        xor ebx,ebx
        
        mov al, [a] ; AL = [a] = 1
        add al, al  ; AL = AL + AL = 1 + 1 = 2
        
        mov bx, [b] ; BX = [b] = 2
        add bx, bx  ; BX = BX + BX = 2 + 2 = 4
        
        cbw ; AX <- AL 2
        
        add ax, bx ; AX = AX + BX = 2 + 4 = 6
        
        mov ebx, [c] ; BX = [c] = 3
        add ebx, ebx  ; BX = BX + BX = 3 + 3 = 6
        
        cwde ; EAX <- AX = 6
        
        add eax, ebx ; EAX = EAX + EBX = 6 + 6 = 12
        
        cdq ; EDX:EAX <- EAX = 12
        
        add EAX, [d]
        adc EDX, [d+2] ; EDX:EAX = EDX:EAX + [d]
    
        
        push    dword 0
        call    [exit]