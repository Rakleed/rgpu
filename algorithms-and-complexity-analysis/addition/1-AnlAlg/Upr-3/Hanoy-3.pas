   PROGRAM Hanoyskie_Bashni;
      Uses CRT;
      type tower = (left,right);
      var numdisk,nummove: LongInt;
          disk           : String[10];
          numear         : Real;
          sm             : Tower;
   { ------------------------------------------------------- }
   PROCEDURE Perekladiyvanie_Diska (n: Integer; sl,sr: Tower);
      PROCEDURE Shag;
      BEGIN
         nummove:=nummove+1; Str(numdisk,disk);
         numear:=nummove / 3.1536E+07
      END;
   BEGIN
      If n=1
        then Shag
        else begin
               Perekladiyvanie_Diska(n-1,sl,sm);
               Shag;
               Perekladiyvanie_Diska(n-1,sm,sr);
             end
   END;
  { --- }
   BEGIN
      nummove:=0;
      Write('��᫮ ��᪮� ?'); Read(numdisk);
      Perekladiyvanie_Diska(numdisk,left,right);
      WriteLn('�६� = ', nummove : length(disk),
                        ' ᥪ = ',numear,' ���');
      WriteLn; ReadKey
   END.

   ��᫮ ��᪮� ? 50
   �६� = 1.12E15 � = 35702052 ���
