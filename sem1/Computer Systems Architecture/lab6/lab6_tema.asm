
; A byte string s is given. Build the byte string d such that every byte d[i] is equal to the count of ones in the corresponding byte s[i] of s.
; Example:
; s: 5, 25, 55, 127
; in binary:
; 101, 11001, 110111, 1111111
; d: 2, 3, 5, 7

bits 32

global start
   
extern exit
import exit msvcrt.dll

segment data use32 class=data

    s db 5,25,55,127
    len_s equ $ - s
    
    d times len_s db 0

segment code use32 class=code
    start:
    
    mov esi, s 
    mov edi, d 
    mov ecx, len_s 
    cld
    
    jecxz end_progr                 ; if the string s is empty skip the loop
    
    repeat:
        push ecx                    ; save the value of ecx
        
        lodsb                       ; load byte from string
        
        mov dl,0                    ; dl is used as a counter
        
        cmp al,0                    ; if read byte has value 0 skip counting its 1 bites
        jz skip_count
        
            count_ones:
                
                shr al,1            ; shift 1 bit to right
                
                jnc skip_inc        ; if CF != 1 jump
                
                    inc dl
                
                skip_inc:           ; only increment dl if shifted bit is 1
                
                cmp al,0            
                
            jnz count_ones          ; this jump is performed until there are no bites with value 1 in al
        
        skip_count:
        
        mov al, dl                  ; al = dl = number of bites with value 1 in the read byte
            
        stosb                       ; store the counter value in d
        
        pop ecx                     ; retrieve the value of ecx
    loop repeat
    
    
        
    end_progr:
        
        push    dword 0
        call    [exit]
