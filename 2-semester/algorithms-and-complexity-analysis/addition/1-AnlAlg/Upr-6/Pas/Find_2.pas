   { ������� ���� � "����஬" �������襣� ������ �������- }
   { �� ����� ������୮�� "��砩����" �᫮���� ���ᨢ�   }
   { -------------------------------------------------------- }
   PROGRAM Find_2;
      uses  CRT;
      const N=7;        { ������⢮ ����⮢ � ���ᨢ�   }
            N1=N+1;     { �����, �� �믮������ N1=N+1    }
      type  R=0..N1;
      var   i: R;       { ��ࠬ��� 横���                  }
            Q: Boolean; { ���� - १���� ���᪠ ����� }
            A: Array [1..N1] of Integer; { ��室�� ���ᨢ }
            X: Integer;                  { �᪮�� ����� }
            c: Char;
   BEGIN
      Write('��室�� ���ᨢ: ');
      For i:=1 to N do
         A[i]:=Random(12)+1;
      For i:=1 to N do
         Write(A[i],' ');
      WriteLn; Write('�᪮�� �����: '); Read(X);
      i:=0; A[N+1]:=X;
      Repeat i:=i+1 until A[i]=X;
      WriteLn;
      If i<>N+1
        then begin
               Write('������� ������; ��� ��������� ');
               WriteLn('������ � ���ᨢ�: ',i)
             end
        else Write('������� �� ������.');
      WriteLn; c:=ReadKey
   END.
