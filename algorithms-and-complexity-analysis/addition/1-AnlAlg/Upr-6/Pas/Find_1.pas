   { ������� ���� �������襣� ������ ��������� ����� }
   { ������୮�� "��砩����" �᫮���� ���ᨢ�            }
   { ----------------------------------------------------- }
   PROGRAM Find_1;
      uses  CRT;
      const N=8;        { ������⢮ ����⮢ � ���ᨢ�   }
      var   i: Integer; { ��ࠬ��� 横���                  }
            Q: Boolean; { ���� - १���� ���᪠ ����� }
            A: Array [1..N] of Integer;  { ��室�� ���ᨢ }
            X: Integer;                  { �᪮�� ����� }
            c: Char;
   BEGIN
      For i:=1 to N do
         A[i]:=Random(12)+1; { ���砩�� ���� ���ᨢ� }
      Write('��室�� ���ᨢ: ');
      For i:=1 to N do 
         Write(A[i],' ');    { ����஫�� �뢮� }
      WriteLn; Write('�᪮�� �����: '); Read(X);
      i:=0;
      Repeat
         i:=i+1; Q:=(A[i]=X)
      until Q OR (i=N);
      WriteLn;
      If Q
        then begin
               Write('������� ������; ��� ��������� ');
               WriteLn('������ � ���ᨢ�: ',i)
             end
        else WriteLn('������� �� ������.');
      c:=ReadKey
   END.
