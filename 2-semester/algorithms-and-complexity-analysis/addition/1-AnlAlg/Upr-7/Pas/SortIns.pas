   { ����஢�� ����묨 ����祭�ﬨ }
   { ------------------------------- }
   PROGRAM SortInsert;
       uses  CRT;
       const N=8;
       type  Index=0..N;
             Massiv=Array[Index] of Integer;
       var   A    : Massiv;
             i,j,k: Index;
             c    : Char;
   BEGIN
      Write('��室�� ���ᨢ: ');
      For i:=1 to N do
         Read(A[i]);
      { ------------------------------------------------- }      
      { ��砫� �����⬠ ���஢�� ����묨 ����祭�ﬨ  }
      { ------------------------------------------------- }
      WriteLn('��������� ���ᨢ� � ����� ���஢��: ');
      WriteLn;
      For i:=2 to N do
         begin
            A[0]:=A[i]; j:=i-1;
            While A[0]<A[j] do 
               begin A[j+1]:=A[j]; j:=j-1 end;
            A[j+1]:=A[0];
            For k:=1 to N do
               Write(A[k],' ');
            WriteLn
         end;
      WriteLn;
      { ----------------------------------------- }
      { ����砭�� ���஢�� ����묨 ����祭�ﬨ }
      { ----------------------------------------- }
      Write('������� ���஢��: ');
      For i:=1 to N do
         Write(A[i],' ');
      WriteLn; c:=ReadKey
   END.
