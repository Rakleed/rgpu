   { � � � � � � � � � � �  ���� �������襣� ������ ��- }
   { �������  �����  ������୮��  "��砩����"  ��ண� }
   { 㯮�冷祭���� �� �����⠭�� �᫮���� ���ᨢ�      }
   { (४��ᨢ�� ��ਠ��)                                }
   { ---------------------------------------------------- }
   PROGRAM Find_5;
      uses  CRT;
      const N = 8;            { ������⢮ ����⮢ � ���ᨢ� }
      type  Massiv = Array [1..N] of Integer;
      var   A     : Massiv;   { ���ᨢ, �����஢���� ��  }
                              { �����⠭��                 }
            Key   : Integer;  { �᪮�� �����             }
            Search: 0..N;     { ������ ���������� �����  }
                              { 0, �᫨ ����� �� ������   }
            Mid    : Integer; { ������ ����७���� ����� }
            j,i    : Integer;
            F1,F2,t: Integer;
            Finish : Boolean;
            c      : Char;
  { ------------------------------------ }
   FUNCTION  F_i_b (N: Integer): Integer;
      var F1,F2: Integer;
   BEGIN
      If (N=0) OR (N=1)
        then F_i_b:=N
        else If N>=2
               then begin
                       F1:=F_i_b (N-1); F2:=F_i_b (N-2);
                       F_i_b:=F1+F2
                    end
   END;
  { --- }
   BEGIN
      Write('������ �����஢���� ���ᨢ: ');
      For i:=1 to N do
         Read(A[i]);
      Write('�᪮�� �����: '); Read(Key);
      j:=1;
      While F_i_b(j)<N+1 do
         j:=j+1;
      Mid:=N-F_i_b(j-2)+1;
      F1:=F_i_b(j-2); F2:=F_i_b(j-3);
      Finish:=FALSE;
      While (Key<>A[Mid]) AND (Finish=FALSE) do
         If (Mid<=0) OR (Key>A[Mid])
           then If F1=1
                  then Finish:=TRUE
                  else begin
                          Mid:=Mid+F2; F1:=F1-F2; F2:=F2-F1
                       end
           else If F2=0
                  then Finish:=TRUE
                  else begin
                          Mid:=Mid-F2; t:=F1-F2; F1:=F2; F2:=t
                       end;
      If Finish
        then Search:=0 
        else Search:=Mid;
      WriteLn;
      WriteLn('������ �᪮���� ����� � ���ᨢ�: ',Search);
      c:=ReadKey
   END.
