   { ������ ���� �������襣� ������ ��������� �- }
   { ���� ������୮�� "��砩����" �᫮���� ���ᨢ�, }
   { ��ண� 㯮�冷祭���� �� �����⠭��              }
   { (��४��ᨢ�� ��ਠ��)                           }
   { ------------------------------------------------- }
   PROGRAM Find_3;
      uses  CRT;
      const N=8;            { ������⢮ ����⮢ � ���ᨢ�    }
      var  i,j,k: Integer;  { ��ࠬ���� 横���                  }
           Q    : Boolean;  { ���� - १���� ���᪠ �����  }
           A    : Array [1..N] of Integer;
                            { ��室�� ���ᨢ, 㯮�冷祭�� �� }
                            { �� �����⠭��                    }
           X    : Integer;  { �᪮�� �����                   }
           c    : Char;
   BEGIN
      WriteLn('���ᨢ ������ ���� ��ண� 㯮�冷祭 �� �����⠭��.');
      Write('������ ������ ���ᨢ�: ');
      For i:=1 to N do
         Read(A[i]);
      Write('�������� ���ᨢ: ');
      For i:=1 to N do
         Write(A[i],' ');
      WriteLn;
      Write('�᪮�� �����: '); Read(X);
      Q:=FALSE; i:=1; j:=N;
      Repeat
         k:=(i+j) DIV 2;
         If A[k]=X
           then Q:=TRUE
           else If A[k]<X
                  then i:=k+1
                  else j:=k-1
      until Q OR (i>j);
      WriteLn;
      If Q
        then begin
               Write('������� ������; ��� ��������� ');
               WriteLn('������ � ���ᨢ�: ',k)
             end
        else WriteLn('������� �� ������.');
      c:=ReadKey
   END.
