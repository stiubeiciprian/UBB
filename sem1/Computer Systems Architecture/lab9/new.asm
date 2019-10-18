global start        

extern exit, scanf, printf, gets
import exit msvcrt.dll
import gets msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    len dd 0                        ; the actual length of the list
    max equ 100                     ; the maximum length of the list
    integers times max db 0         ; the list of integers
    
    msg_r db "Enter a list of integers separated by spaces: ", 0
    
    format_r db "%s", 0
    format_p db "The list of integers: %s", 0

; This program reads a list of integers separated by spaces.
; The reading ends when the user hits ENTER.
segment code use32 class=code
start:
    ; display a message to user
    push dword msg_r
    call [printf]
    add esp, 4*1

    ; read from the keyboard until user hit ENTER
    push dword integers
    call [gets]
    add esp, 4*1
    
    ; display the list of integers
    push dword integers
    push dword format_p
    call [printf]
    add esp, 4*2
    
    ; exit(0)
    push dword 0      ; push the parameter for exit onto the stack
    call [exit]       ; call exit to terminate the program