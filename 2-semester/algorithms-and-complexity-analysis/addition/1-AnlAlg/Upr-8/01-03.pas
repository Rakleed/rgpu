   { ���������� ������室���� �����⬠ ��宦�����  �� }
   { �ᥣ� ������饣��� ����� � 楫��᫥���� �������- }
   { ��� ���ᨢ�, ����� ᮤ�ন� N ����⮢, � ������� }
   { ����� ����砥��� � ���ᨢ� ����� N/2 ࠧ            }
   { ------------------------------------------------------ }
   PROGRAM Primer_3;
      Uses  CRT;
      const N=11;
       type R=1..N;
            Q=Array[R] of Integer;
        var A: Q;
            k: Integer;
            i: Integer; { ��६�饭�� �� ���ᨢ�             }
            m: Integer; { ��६����� ��� �࠭���� ������⢠ }
                        { ����७�� ����� ���ᨢ�        }
   { ------------------------------------------------------- }
   BEGIN
      Randomize;
      Write('��室�� ���ᨢ: ');
      k:=1;
      While k<=N do
        begin A[k]:=Random(3)+1; k:=k+2 end;
      k:=2;
      While k<=N do
        begin A[k]:=Random(3)+1; k:=k+2 end;
      For k:=1 to N do
        Write(A[k]:2,' ');
      WriteLn;
      { ------- }
      k:=0; i:=0;
      While i<>N do
        If k=0
          then begin k:=1; m:=i+1; i:=i+1 end
          else If A[i+1]=A[m]
                 then begin i:=i+1; k:=k+1 end
                 else begin i:=i+1; k:=k-1 end;
      WriteLn;
      Write('������� �㤥� ������, �᫨ ���ᨢ ');
      WriteLn('"���஥�" ���ࠢ��쭮!');
      Write('�������      : ',A[m]:2,' '); WriteLn;
      ReadKey
   END.
