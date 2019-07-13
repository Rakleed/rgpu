; (c) xrnd [2010] [http://asmworld.ru/]
; inputhex.asm - ���� ����������������� �����

use16			    ;������������ 16-������ ���
org 100h		    ;��������� ���������� � ������ 100h

    mov cx,print_str	    ;����� ��������� print_str
    mov bx,print_endline    ;����� ��������� print_endline

in_byte_lp:
    mov di,s_byte
    call cx		    ;����� ������ 'byte:'
    call input_hex_byte     ;���� �����
    call bx		    ;����� ����� ������
    jnc in_word_lp	    ;���� ��� ������, ������� � ����� �����
    mov di,s_error
    call cx		    ;����� ������ 'ERROR!'
    jmp in_byte_lp	    ;������� � ������ �����

in_word_lp:
    mov di,s_word
    call cx		    ;����� ������ 'word:'
    call input_hex_word     ;���� �����
    call bx		    ;����� ����� ������
    jnc exit		    ;���� ��� ������, ������� � ������ �� ���������
    mov di,s_error
    call cx		    ;����� ������ 'ERROR!'
    jmp in_word_lp	    ;������� � ������ �����

exit:
    mov di,s_pak
    call cx		    ;����� ������ 'Press any key...'
    mov ah,8		    ;������� DOS 08h - ���� ������� ��� ���
    int 21h

    mov ax,4C00h	    ;\
    int 21h		    ;/ ���������� ���������

;-------------------------------------------------------------------------------
;��������� ����� ����� � ������� � ����������������� ����
; �����: AL - ���� (� ������ ������ AL = 0)
;        CF = 1 - ������
input_hex_byte:
    push dx		    ;���������� DX
    mov al,3		    ;���� �������� 2 �������� (FF) + ����� ������
    call input_str	    ;����� ��������� ����� ������
    call str_to_hex_byte    ;�������������� ������ � ����
    pop dx		    ;�������������� DX
    ret

;-------------------------------------------------------------------------------
;��������� ����� ����� � ������� � ����������������� ����
; �����: AX - ����� (� ������ ������ AX = 0)
;        CF = 1 - ������
input_hex_word:
    push dx		    ;���������� DX
    mov al,5		    ;���� �������� 4 �������� (FFFF) + ����� ������
    call input_str	    ;����� ��������� ����� ������
    call str_to_hex_word    ;�������������� ������ � �����
    pop dx		    ;�������������� DX
    ret

;-------------------------------------------------------------------------------
;��������� �������������� ����������������� ������ � ����
;  ����: AL - ����� ������
;        DX - ����� ������, ��������������� �������� CR(0Dh)
; �����: AL - ���� (� ������ ������ AL = 0)
;        CF = 1 - ������
str_to_hex_byte:
    push cx		    ;���������� CX
    mov cx,ax		    ;���������� AX � CX
    cmp al,2		    ;�������� ����� ������
    jg sthb_error	    ;���� ������ 2, ���������� ������
    call str_to_hex_word    ;�������������� ������ � �����
    jnc sthb_exit	    ;���� ��� ������, �� ������� � ������ �� ���������
sthb_error:
    stc 		    ;CF = 1
sthb_exit:
    mov ah,ch		    ;�������������� AH
    pop cx		    ;�������������� CX
    ret

;-------------------------------------------------------------------------------
;��������� �������������� ����������������� ������ � �����
;  ����: AL - ����� ������
;        DX - ����� ������, ��������������� �������� CR(0Dh)
; �����: AX - ����� (� ������ ������ AX = 0)
;        CF = 1 - ������
str_to_hex_word:
    push cx		    ;���������� ���������
    push dx
    push si

    movzx cx,al 	    ;CX = ������� ����� = ����� ������
    jcxz sthw_error	    ;���� ����� ������ = 0, ���������� ������
    cmp cx,4
    jg sthw_error	    ;���� ����� ������ ������ 4, ���������� ������
    xor ax,ax		    ;AX = 0
    mov si,dx		    ;SI = ����� ������

sthw_lp:
    mov dl,[si] 	    ;�������� � DL ���������� ������� ������
    inc si		    ;��������� ������ ������
    call convert_hex_digit  ;�������������� ����������������� ����� � �����
    jc sthw_error	    ;���� ������, �� ���������� ������
    shl ax,4		    ;����� AX �� 4 ���� �����
    or al,dl		    ;���������� ��������������� �����
    loop sthw_lp	    ;������� �����
    jmp sthw_exit	    ;CF = 0

sthw_error:
    xor ax,ax		    ;AX = 0
    stc 		    ;CF = 1

sthw_exit:
    pop si		    ;�������������� ���������
    pop dx
    pop cx
    ret

;-------------------------------------------------------------------------------
;��������� �������������� ����������������� ����� � �����
;  ����: DL - ������-�����
; �����: DL - �������� ����� (0-15, � ������ ������ DL = 0)
;        CF = 1 - ������
convert_hex_digit:
    cmp dl,'0'		    ;��������� � �������� '0'
    jl chd_error	    ;���� ������, ���������� ������
    cmp dl,'9'		    ;��������� � �������� '9'
    jg chd_a_f		    ;���� ������, �� �������� ��� ����� a-f ��� A-F
    sub dl,'0'		    ;�������������� ����� � �����
    ret 		    ;������� �� ��������� (����� ������ CF = 0)

chd_a_f:
    and dl,11011111b	    ;�������������� ����� � ������� �������
    cmp dl,'A'		    ;��������� � �������� 'A'
    jl chd_error	    ;���� ������, ���������� ������
    cmp dl,'F'		    ;��������� � �������� 'F'
    jg chd_error	    ;���� ������, ���������� ������
    sub dl,'A'-10	    ;����������� ����� � �����
    ret 		    ;������� �� ��������� (����� ���� ������ CF = 0)

chd_error:
    xor dl,dl		    ;DL = 0
    stc 		    ;CF = 1
    ret 		    ;������� �� ���������

;-------------------------------------------------------------------------------
;��������� ����� ������ c �������
;  ����: AL - ������������ ����� (� �������� CR) (1-254)
; �����: AL - ����� �������� ������ (�� ������ ������� CR)
;        DX - ����� ������, ��������������� �������� CR(0Dh)
input_str:
    push cx		    ;���������� �X
    mov cx,ax		    ;���������� AX � CX
    mov ah,0Ah		    ;������� DOS 0Ah - ���� ������ � �����
    mov [buffer],al	    ;������ ������������ ����� � ������ ���� ������
    mov byte[buffer+1],0    ;��������� ������� ����� (����������� �����)
    mov dx,buffer	    ;DX = a���� ������
    int 21h		    ;��������� � ������� DOS
    mov al,[buffer+1]	    ;AL = ����� �������� ������
    add dx,2		    ;DX = ����� ������
    mov ah,ch		    ;�������������� AH
    pop cx		    ;�������������� CX
    ret

;-------------------------------------------------------------------------------
;��������� ������ ������ �� �������
; DI - ����� ������
print_str:
    push ax
    mov ah,9		    ;������� DOS 09h - ����� ������
    xchg dx,di		    ;����� ���������� DX � DI
    int 21h		    ;��������� � ������� DOS
    xchg dx,di		    ;����� ���������� DX � DI
    pop ax
    ret

;-------------------------------------------------------------------------------
;��������� ������ ����� ������ (CR+LF)
print_endline:
    push di
    mov di,endline	    ;DI = ����� ������ � ��������� CR,LF
    call print_str	    ;����� ������ �� �������
    pop di
    ret

;-------------------------------------------------------------------------------
; ������
s_byte	 db 'byte: $'
s_word	 db 'word: $'
s_error  db 'ERROR!',13,10,'$'
s_pak	 db 'Press any key...$'
endline  db 13,10,'$'
buffer	 rb 7
