;Read two numbers a and b (base 10) from the keyboard and calculate: (a+b)*(a-b). The result of multiplication will be stored in a variable called "result" (defined in the data segment).

bits 32

global start
   
extern printf, scanf, exit
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data
    a db 0
    b db 0
    result resb 4
    format_scan db "%d", 0
    msg_a db "Enter number a: ", 13, 10, 0
    msg_b db "Enter number b: ", 13, 10, 0
    format_print db "(a+b)*(a-b) = %d", 0
segment code use32 class=code
    start:
        
        
        ;print the message: "Enter number a:"
        push dword msg_a
        call [printf]
        add esp, 4 * 1
        
        ;read the number a from keyboard
        push dword a
        push dword format_scan
        call [scanf]
        add esp, 4 * 2      ; clean stack
        
        
        ;print the message: "Enter number b:"
        push dword msg_b
        call [printf]
        add esp, 4 * 1
        
        ;read the number b from keyboard
        push dword b
        push dword format_scan
        call [scanf]
        add esp, 4 * 2      ; clean stack
        
        ;(a+b)*(a-b)
        mov ax, [a]    ; ax := [a]
        sub ax, [b]    ; ax := ax - [b]
        
        mov bx, [a]    ; bx := [a]
        add bx, [b]    ; bx := bx + [b]
        
        imul bx        ; dx:ax := ax * bx
        mov [result], ax
        mov [result + 2], dx  ; result := dx:ax
        
        ;print result
        push dword [result]
        push dword format_print
        call [printf]
        add esp, 4 * 2
        
        
        push dword 0
        call [exit]
