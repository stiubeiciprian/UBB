; Read from file numbers.txt a string of numbers (positive and negative). Build two strings using readen numbers:
; P – only with positive numbers
; N – only with negative numbers
; Display the strings on the screen.

; Input file contains a string of numbers separated by spaces.
; Ex: 
;           1 -21 23 4 -2
; Output:
;           1 23 4      ;str_pos
;           -21 -2      ;str_neg


bits 32

global start


extern exit, fopen, fread, fclose, printf, fprintf
import exit msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll

extern split

global str_neg
global str_pos

segment data use32 public class=data 
    file_name db "numbers.txt", 0
    read_mode db "r", 0
    file_descriptor dd -1
    len equ 100
    text times (len+1) db 0
    str_pos resb 50
    str_neg resb 50
    format_print_neg db "Negative string:", 10, 13, " %s", 10, 13, 0
    format_print_pos db "Positive string:", 10, 13, " %s", 10, 13, 0

segment code use32 class=code

    start:
        ; Open file to read
        push dword read_mode
        push dword file_name
        call [fopen]
        add esp, 4*2

        mov [file_descriptor], eax  ; store the file descriptor returned by fopen

        ; Check for errors
        cmp eax, 0
        je final
        
        ; Read from file
        push dword [file_descriptor]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        ; Split in 2 strings
        mov ecx, eax                    ; ecx:= eax = numbers of chars read
        mov esi, text
        call split

        ; Close the file
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        

        ; print positive string
        push dword str_pos
        push dword format_print_pos
        call [printf]
        add esp, 4 * 2
        
        ; print negative string
        push dword str_neg
        push dword format_print_neg
        call [printf]
        add esp, 4 * 2

      final:

        ; exit(0)
         push dword 0
         call [exit]
