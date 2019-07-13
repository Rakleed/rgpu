   { ���������� ���᫥��� ��᫥����⥫쭮��, �������� }
   { ४��७�� ᮮ⭮襭��� ��ࢮ�� ���浪�:           }
   {                                                      }
   {  F(1)=2, F(n)=3*F(n-1), n=2,3,...                    }
   {                                                      }
   { ���������� ��।������ �६��� ���᫥���          }
   { ---------------------------------------------------- }
   PROGRAM Primer_1_1;
      Uses  DOS, { ������⥪�, ᮤ�ঠ�� ��楤��� GetTime }
            CRT; { ������⥪�, ᮤ�ঠ�� ��楤��� ClrScr  }
      const C1= 1;
            C2=15;
      var   H0,M0,S0,s0100,H1,M1,S1,S1100: Word;
            k: LongInt;
  { ------------------------------------- }
   FUNCTION Prim_1_1 (n: Integer): LongInt;
   { �����ᨢ��� ���᫥��� ����� ��᫥��- }
   { ��⥫쭮�� � ����஬ n                  }
   { ---------------------------------------- }
   BEGIN
      If n=1
        then Prim_1_1:=3
        else Prim_1_1:=3*Prim_1_1(n-1)
   END;
  { ----------------------------------- }
   FUNCTION Prim_2_3 (n: Integer): Real;
   { ��४��ᨢ��� ���᫥��� ����� ��᫥��- }
   { ��⥫쭮�� � ����஬ n                    }
   { ------------------------------------------ }
   BEGIN
      Prim_2_3:=Exp(n*Ln(3.0))
   END;
  { ---------------------------------------- }
   FUNCTION WorkTime(Hour0,Min0,Sec0,sec0100,
                     Hour1,Min1,Sec1,Sec1100: Word): Real;
   { �㭪�� ������ �६�, � ᥪ㭤��, �� ��砫쭮�� }
   { �� ����筮�� �����⮢ ࠡ��� �ࠣ���� �ணࠬ��:  }
   { Hour0 : Min0 : Sec0 : Sec0100 - ��砫쭮� �६�    }
   { Hour1 : Min1 : Sec1 : Sec1100 - ����筮� �६�     }
   { (���, ������, ᥪ㭤�, 1/100 ᥪ㭤�)             }
   { -------------------------------------------------- }
      var OldTime: Real;   { ��砫쭮� �६� � ᥪ㭤�� }
          NewTime: Real;   { ����筮� �६� � ᥪ㭤��  }
   BEGIN
      OldTime:=Hour0*60*60+Min0*60+Sec0+Sec0100/100;
      NewTime:=Hour1*60*60+Min1*60+Sec1+Sec1100/100;
      WorkTime:=NewTime-OldTime
   END;
  { --- }
   BEGIN
      ClrScr;
      WriteLn('�����ᨢ��� ���᫥���: ');
      For k:=C1 to C2 do
        begin
          GetTime(H0,M0,S0,S0100);
          Write('  Prim_1_1(',k:2,')=',Prim_1_1(k):8,'  ');
          GetTime(H1,M1,S1,S1100);
          WriteLn(WorkTime(H0,M0,S0,S0100,H1,M1,S1,S1100):5:2,' ᥪ');
        end;
      WriteLn;
      WriteLn('��४��ᨢ��� ���᫥���: ');
      For k:=C1 to C2 do
        begin
          GetTime(H0,M0,S0,S0100);
          Write('  Prim_2_3(',k:2,')=',Prim_2_3(k):8:0,'  ');
          GetTime(H1,M1,S1,S1100);
          WriteLn(WorkTime(H0,M0,S0,S0100,H1,M1,S1,S1100):5:2,' ᥪ');
        end;
      WriteLn;
      ReadKey
   END.
