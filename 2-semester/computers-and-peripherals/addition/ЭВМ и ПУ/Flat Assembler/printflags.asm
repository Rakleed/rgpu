; (c) xrnd [2010] [http://asmworld.ru/]
; printflags.asm - ����� �� ������� ��������� ������ SF, ZF, AF, PF � CF.

use16			    ;������������ 16-������ ���
org 100h		    ;��������� ���������� � ������ 100h
    jmp start		    ;������� �� ����� start
;---------------------------------------------------------------------
; ������
s_sf	db 'FLAGS: SF=$'
s_zf	db ' ZF=$'
s_af	db ' AF=$'
s_pf	db ' PF=$'
s_cf	db ' CF=$'
s_endl	db 13,10,'$'
s_pak	db 'Press any key...$'
;---------------------------------------------------------------------
start:
    mov al,120
    add al,56		    ;������ �������������� ��������
    call print_flags	    ;����� ��������� ������ ��������� ������
    cmc 		    ;�������� ����� CF
    call print_flags	    ;����� ��������� ������ ��������� ������
    xor ax,ax		    ;������ ���������� ��������
    call print_flags	    ;����� ��������� ������ ��������� ������

    mov ah,9
    mov dx,s_pak
    int 21h		    ;����� ������ 'Press any key...'
    mov ah,8		    ;������� DOS 08h - ���� ������� ��� ���
    int 21h

    mov ax,4C00h	    ;\
    int 21h		    ;/ ���������� ���������

;----------------------------------------------------------------------
;��������� ������ ��������� ������ �� �������
print_flags:
    push ax
    push cx
    push dx
    pushf		    ;���������� �������� ������
    lahf		    ;�������� �������� ����� FLAGS � AH
    mov cl,ah		    ;CL = AH
    mov ah,9		    ;������� DOS 09h - ����� ������
    mov dx,s_sf 	    ;DX = ����� ������ 'FLAGS: SF='
    int 21h		    ;��������� � ������� DOS
    shl cl,1		    ;����� CL ����� �� 1 ���
    call print_cf	    ;������ ����������� ����
    mov dx,s_zf
    int 21h		    ;����� ������ ' ZF='
    shl cl,1		    ;����� CL ����� �� 1 ���
    call print_cf	    ;������ ����������� ����
    mov dx,s_af
    int 21h		    ;����� ������ ' AF='
    shl cl,2		    ;����� CL ����� �� 2 ����
    call print_cf	    ;������ ����������� ����
    mov dx,s_pf
    int 21h		    ;����� ������ ' PF='
    shl cl,2		    ;����� CL ����� �� 2 ����
    call print_cf	    ;������ ����������� ����
    mov dx,s_cf
    int 21h		    ;����� ������ ' CF='
    shl cl,2		    ;����� CL ����� �� 2 ����
    call print_cf	    ;������ ����������� ����
    mov dx,s_endl
    int 21h		    ;����� ����� ������
    popf		    ;�������������� �������� ������
    pop dx
    pop cx
    pop ax
    ret

;----------------------------------------------------------------------
;��������� ������ �������� ����� CF � ���� �������
print_cf:
    push ax
    push dx
    mov ah,2		    ;������� DOS 02h - ����� �������
    mov dl,'0'		    ;DL = '0'
    adc dl,0		    ;���� CF = 1, �� � DL ����� ������ '1'
    int 21h		    ;��������� � ������� DOS
    pop dx
    pop ax
    ret