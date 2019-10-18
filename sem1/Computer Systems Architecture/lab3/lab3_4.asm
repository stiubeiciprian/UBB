;Write a program in assembly language which computes one of the following arithmetic expressions, considering the following domains for the variables (in the unsigned and signed representation).
; (a*b-2*c*d)/(c-e)+x/a
; a,b,c,d-byte; e-word; x-qword
; SIGNED
bits 32

global start
   
extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 4
    b db 6
    c db 2
    d db 3
    e dw 3
    x dq 16
    
segment code use32 class=code
    start:
    ;(a*b-2*c*d)/(c-e)
        xor eax,eax
        xor ebx,ebx
        xor edx,edx
        
        mov al, [a] ; AL = [a] = 4
        imul byte [b] ; AX = AL * [b] = 4 * 6 =24
        
        push word ax ; top stack byte = AX = 24
        
        mov al, 2 ; AL = 2
        imul byte [c] ; AX = 2 * [c] = 2 * 2 = 4
        
        mov bx, ax ; BX = AX = 4
        
        mov al, [d] ; AL = [d] = 3
        cbw ; AX <- AL = 3
        
        imul bx ; DX:AX = AX * BX = 3 * 4 = 12
        
        push word dx ; high part
        push word ax ; low part
        
        pop ebx ; EBX = DX:AX = 12
        pop ax ; AX = 24
        
        cwde ; EAX <- AX = 24
        
        sub eax, ebx ; EBX = EBX - EAX = 24 - 12 = 12
        
        push dword eax;  = EAX = 12
        
        
        
        mov al, [c] ; AL = [c] = 2
        
        cbw ; AX <- AL = 2
        
        sub ax, [e] ; AX = AX - [e] = 2 - 3 = -1
        
        mov bx, ax ; BX = AX = -1
        
        
        pop ax ; AX = low part
        pop dx ; DX = high part   DX:AX = 12
       
        idiv bx ; AX = DX:AX / BX = 12 / -1 = -12
       
        push word ax ;  = AX = -12
        
    ;x/a    
        mov al, [a] ; AL = [a] = 4
        cbw ; AX <- AL = 4
        cwde ; EAX <- AX = 4
        mov ebx, eax ; EBX = EAX = 4
        
        
        mov eax, [x] ; low part of x
        mov edx, [x+2] ; high part of x    EDX: EAX = [x] = 16
        
        idiv ebx ; EAX = EDX:EAX / EBX = 16 / 4 = 4
        
     
     ;(a*b-2*c*d)/(c-e)+x/a
        pop word ax ; AX = -12
        
        cwde ; EAX <- AX = -12
        
        add eax, ebx ; EAX = EAX + EBX = -12 + 4 = -8
      
        
        push    dword 0
        call    [exit]
