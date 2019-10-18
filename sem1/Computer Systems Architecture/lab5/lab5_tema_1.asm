
; Two byte strings A and B are given. Obtain the string R by concatenating the elements of B in reverse order and the elements of A in reverse order.
; Example:
; A: 2, 1, -3, 0
; B: 4, 5, 7, 6, 2, 1
; R: 1, 2, 6, 7, 5, 4, 0, -3, 1, 2


; a: 4,5
; b: 1,2,3
; r: 3,2,1,5,4

bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data

    a db '4', '5'       ;2, 1, -3, 0
    a_len equ $ - a
    
    b db '1', '2', '3'  ;4, 5, 7, 6, 2, 1
    b_len equ $ - b
    
    r_len equ $ - a
    r times r_len db 0

segment code use32 class=code
    start:
        
        mov esi, b + b_len-1    ; source index = b 
        mov edi, r          ; destination index = r 
        mov ecx, b_len      ; ecx = b_len
        
        jecxz second_str    ; if first string is empty jump to second_str
        
        
        rep_str_1:
            
            std             ; DF = 1 , set direction flag to start reading from the last byte of the string
            lodsb
            
            cld             ; DF = 0 , clear direction flag to store bytes in r 
            stosb
            
        loop rep_str_1      ; reads string b and stores it in reverse order in r
        
        
        second_str:
        
        mov esi, a + a_len-1  ; source index = a
        mov ecx, a_len      ; ecx = a_len
        
        jecxz end_program   ; if second string is empty jump to end_program
        
        
        rep_str_2:
            
            std             ; DF = 1 , set direction flag to start reading from the last byte of the string
            lodsb
            
            cld             ; DF = 0 , clear direction flag to store bytes in r 
            stosb
            
        loop rep_str_2      ; reads string a and stores it in reverse order in r
        
        
        end_program:
        
        push    dword 0
        call    [exit]
