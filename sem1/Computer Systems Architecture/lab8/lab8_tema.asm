
;A file name and a text (defined in the data segment) are given. The text contains lowercase letters, uppercase letters, digits and special characters. Transform all the lowercase letters from the given text in uppercase. Create a file with the given name and write the generated text to file.

bits 32

global start

; declare external functions needed by our program
extern exit, fopen, fread, fclose, printf, fprintf
import exit msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    file_name db "input.txt", 0
    read_mode db "r", 0       
    write_mode db "w", 0        
    file_descriptor dd -1
    len equ 100
    text times (len+1) db 0

; our code starts here
segment code use32 class=code
    start:
        ; Open file to read
        push dword read_mode     
        push dword file_name
        call [fopen]
        add esp, 4*2                ; clean-up the stack

        mov [file_descriptor], eax  ; store the file descriptor returned by fopen

        ; Check for errors
        cmp eax, 0
        je final

        ; Read text from file
        push dword [file_descriptor]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4

        ; Transform every lowercase letter to uppercase
        
        mov ecx, eax    ; ecx := eax = number of chars we've read 
        mov esi, text
        mov edi, text
        cld
        
        upper:
        
            lodsb   ; load character
            
            ; if current character is not a letter ( <'a' or >'b') jump to .skip:
            cmp eax, 'a'
            JL .skip        
            
            cmp eax, 'z'
            JG .skip
            
            
            sub eax, 32 ; eax := eax - 32 , character is transformed to uppercase
            
            .skip:
            stosb   ;store character
            
        loop upper
        
        ;Close the file
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        
        
       ; Open file to write
        push dword write_mode     
        push dword file_name
        call [fopen]
        add esp, 4*2                ; clean-up the stack
        
        ; Check for errors
        cmp eax, 0
        je final
        
        ; Write new text to file
        ; fprintf(file_descriptor, text)
        push dword text
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4*2
        
        ; Close file
        ; fclose(file_descriptor)
        push dword [file_descriptor]
        call [fclose]
        add esp, 4

      final:

        ; exit(0)
        push dword 0
        call [exit]