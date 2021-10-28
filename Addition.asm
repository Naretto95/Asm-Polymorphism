section .text
global _start
_start:

mov r12,0x4	       	; 4 -> r12
add r12,0x4	      	; r12 += 4
add r12,0x30	    ; r12 en ascii
push r12			; on envoie r12
mov rax,0x1			; on prepare le syscall
mov rdi,0x1
mov rsi,rsp			; on pointe vers le haut de la pile
mov rdx,0x1 		
syscall 
mov rcx, 0x0A       ; \n 
push rcx            ; on le push
mov rsi, rsp        ; on pointe vers le haut de la pile
syscall
mov rax,60			
mov rdi,0	
syscall
