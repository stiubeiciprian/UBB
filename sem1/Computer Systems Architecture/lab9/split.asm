bits 32

global split

extern str_neg, str_pos
                    
segment code use32 class=code

split:
        mov edi, 0     ; used as index for str_pos
        mov edx, 0     ; used as index for str_neg
        cld
        
        repeta:
        
            lodsb
        
            cmp al, " "
            je .next_num
            
            cmp al, "-"
            je .negative
            
            ; Add number to positive string
            
            .positive:
                mov [str_pos + edi], al
                inc edi
                
                lodsb
                dec ecx         ; load another char
                jz end_of_file
                
                cmp al, " "
            jne .positive
            
            mov byte [str_pos + edi], 32
            inc edi                         ; Add space after positive numbers
            
            jmp .next_num
            
            
            ;Add number to negative string
            .negative:
                mov [str_neg + edx], al
                inc edx
                
                lodsb
                dec ecx         ; load another char
                jz end_of_file
                
                cmp al, " "
            jne .negative
            
            
            mov byte [str_neg + edx], 32
            inc edx                         ; Add space after negative numbers
                
            .next_num:
        loop repeta
        end_of_file:
        ret
        