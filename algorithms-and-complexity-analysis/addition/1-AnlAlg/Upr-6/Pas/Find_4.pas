   { � � � � � � � �  ���� �������襣� ������ ��������� }
   { ����� ������୮�� "��砩����" �᫮���� ���ᨢ�, }
   { ��ண� 㯮�冷祭���� �� �����⠭��                 }
   { (४��ᨢ�� ��ਠ��)                                }
   { ---------------------------------------------------- }
   PROGRAM Find_4;
      uses  CRT;
      const N=8;               { ������⢮ ����⮢ }
       type Massiv = Array [1..N] of Integer;
        var A       : Massiv;  { ���ᨢ, �����஢���� }
                               { �� �����⠭��          }
            Key     : Integer; { �᪮�� �����         }
            i       : Integer;
            c       : Char;
   { ---------------------------- }
   FUNCTION BinSearch(A   : Massiv;
                      Low : Integer;
                      High: Integer;
                      X   : Integer): Integer;
      var Mid: Integer; { "�।���" ������ ����⮢ ���ᨢ� }
   BEGIN
      If Low>High
        then BinSearch:=0
        else begin
                Mid:=(Low+High) DIV 2;
                If X=A[Mid]
                  then BinSearch:=Mid
                  else If X<A[Mid]
                         then BinSearch:=BinSearch(A,Low,Mid-1,X)
                         else BinSearch:=BinSearch(A,Mid+1,High,X)
             end
   END;
  { --- }
   BEGIN
      Write('������ ���ᨢ, �����஢���� ��ண� �� �����⠭��: ');
      For i:=1 to N do
        Read(A[i]);
      Write('�᪮�� �����: '); Read(Key);
      WriteLn;
      If BinSearch(A,1,N,Key)=0
        then WriteLn('�᪮�� ����� �� ������.')
        else WriteLn('�᪮�� ����� ����� � ���ᨢ� ������ ',
                      BinSearch(A,1,N,Key));
      c:=ReadKey
   END.
