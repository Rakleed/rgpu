   { ��� �������� ���ᨢ X. �� ��� ������, �� ࠢ�� }
   { ���, ��९���� (��࠭�� �� ���冷�) � ��砫� ���- }
   { ᨢ�, � �㫥�� ������ - � ����� ���ᨢ� (�� �⮬ }
   { ���� ���ᨢ �� �ᯮ�짮����)                        }
   { ---------------------------------------------------- }
   PROGRAM v14;
      Uses CRT;
      var k,
          n,
          i: Integer; 
          X: Array [1..8] of Integer;
   BEGIN
     k:=0;
     Write('������ n: '); ReadLn(n);
     for i:=1 to n do
       Read(X[i]);
     for i:=1 to n do
       if X[i]<>0
         then X[i-k]:=X[i]
         else k:=k+1;
     for i:=n-k+1 to n do
       X[i]:=0;
     Write('�������: ');
     For i:=1 to n do
       Write(X[i],' ');
     ReadKey
   END.
