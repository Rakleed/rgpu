   { ����஢�� ��⮤�� ���⮣� �롮� }
   { (���� ᯮᮡ)                    }
   { ---------------------------------- }
   PROGRAM SortChoice_1;
      uses  CRT;
      const N=8;
      type  Index=1..N;
            Massiv=Array[Index] of Integer;
       var  x      : Integer;
            A      : Massiv;
            i,j,k,m: Index;
            c      : Char;
   BEGIN
      Write('��室�� ���ᨢ: ');
      For i:=1 to N do
         Read(A[i]);
      { -------------------------------------------------- }
      { ��砫� �����⬠ ���஢�� ����� �롮஬        }
      { -------------------------------------------------- }
      WriteLn ('��������� ���ᨢ� � ����� ���஢��: ');
      WriteLn;
      For i:=1 to N-1 do
         begin
            k:=i; x:=A[i];
            For j:=i+1 to N do
              If A[j]<x
                then begin k:=j; x:=A[j] end;
            A[k]:=A[i]; A[i]:=x;
            For m:=1 to N do
               Write(A[m],' ');
            WriteLn
         end;
      WriteLn;
      { ---------------------------------------------- }
      { ����砭�� �����⬠ ���஢�� ����� �롮஬ }
      { ---------------------------------------------- }
      Write('������� ���஢��: ');
      For i:=1 to N do
         Write(A[i],' ');
      WriteLn; c:=ReadKey
   END.
