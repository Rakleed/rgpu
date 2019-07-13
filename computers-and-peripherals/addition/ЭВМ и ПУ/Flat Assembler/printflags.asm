; (c) xrnd [2010] [http://asmworld.ru/]
; printflags.asm - вывод на консоль состояния флагов SF, ZF, AF, PF и CF.

use16			    ;Генерировать 16-битный код
org 100h		    ;Программа начинается с адреса 100h
    jmp start		    ;Переход на метку start
;---------------------------------------------------------------------
; Данные
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
    add al,56		    ;Пример арифметической операции
    call print_flags	    ;Вызов процедуры вывода состояния флагов
    cmc 		    ;Инверсия флага CF
    call print_flags	    ;Вызов процедуры вывода состояния флагов
    xor ax,ax		    ;Пример логической операции
    call print_flags	    ;Вызов процедуры вывода состояния флагов

    mov ah,9
    mov dx,s_pak
    int 21h		    ;Вывод строки 'Press any key...'
    mov ah,8		    ;Функция DOS 08h - ввод символа без эха
    int 21h

    mov ax,4C00h	    ;\
    int 21h		    ;/ Завершение программы

;----------------------------------------------------------------------
;Процедура вывода состояния флагов на консоль
print_flags:
    push ax
    push cx
    push dx
    pushf		    ;Сохранение регистра флагов
    lahf		    ;Загрузка младшего байта FLAGS в AH
    mov cl,ah		    ;CL = AH
    mov ah,9		    ;Функция DOS 09h - вывод строки
    mov dx,s_sf 	    ;DX = адрес строки 'FLAGS: SF='
    int 21h		    ;Обращение к функции DOS
    shl cl,1		    ;Сдвиг CL влево на 1 бит
    call print_cf	    ;Печать выдвинутого бита
    mov dx,s_zf
    int 21h		    ;Вывод строки ' ZF='
    shl cl,1		    ;Сдвиг CL влево на 1 бит
    call print_cf	    ;Печать выдвинутого бита
    mov dx,s_af
    int 21h		    ;Вывод строки ' AF='
    shl cl,2		    ;Сдвиг CL влево на 2 бита
    call print_cf	    ;Печать выдвинутого бита
    mov dx,s_pf
    int 21h		    ;Вывод строки ' PF='
    shl cl,2		    ;Сдвиг CL влево на 2 бита
    call print_cf	    ;Печать выдвинутого бита
    mov dx,s_cf
    int 21h		    ;Вывод строки ' CF='
    shl cl,2		    ;Сдвиг CL влево на 2 бита
    call print_cf	    ;Печать выдвинутого бита
    mov dx,s_endl
    int 21h		    ;Вывод конца строки
    popf		    ;Восстановление регистра флагов
    pop dx
    pop cx
    pop ax
    ret

;----------------------------------------------------------------------
;Процедура вывода значения флага CF в виде символа
print_cf:
    push ax
    push dx
    mov ah,2		    ;Функция DOS 02h - вывод символа
    mov dl,'0'		    ;DL = '0'
    adc dl,0		    ;Если CF = 1, то в DL будет символ '1'
    int 21h		    ;Обращение к функции DOS
    pop dx
    pop ax
    ret