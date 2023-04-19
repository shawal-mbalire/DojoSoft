; creating a hello world program in assembly

;creating text in section
section .data
    text db "Hello, World!",10

;starting global function
section .text
    global _start

;onstart
_start:
;hex values of where to print the hello world text
    mov rax, 1
    mov rdi, 1
    mov rsi, text
    mov rdx, 14
    syscall
 
    mov rax, 60
    mov rdi, 0
    syscall