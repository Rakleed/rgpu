   { � ���ᨢ� X ����� ����� ࠢ�� 1 ��� 2. ����⠢�� }
   { ������ ���ᨢ� ⠪, �⮡� ���砫� �ᯮ�������� �� }
   { 0, ��⥬ - �� 1 �, �������, �� 2 (�� �⮬ �������- }
   { ⥫�� ���ᨢ �� �ᯮ�짮����)                       }
   { ----------------------------------------------------- }
   PROGRAM v15;
      Uses CRT;
      var m,
          n0,n1,n2,
          i: Integer; 
          x: Array [1..8] of 0..2;
   BEGIN
     n0:=0; n1:=0; n2:=0;
     Write('������ m: '); Read(m);
     for i:=1 to m do
       Read(x[i]);
     For i:=1 to m do
       Case x[i] of
         0: n0:=n0 + 1;
         1: n1:=n1 + 1;
         2: n2:=n2 + 1
       end;
     For i:=1 to n0 do
       x[i]:=0;
     For i:=n0+1 to n0+n1 do
       x[i]:=1;
     For i:=n0+n1+1 to m do
       x[i]:=2;
     Write('������஢���� ���ᨢ: ');
     For i:=1 to m do
       Write(' ',x[i]);
     ReadKey
   END.
