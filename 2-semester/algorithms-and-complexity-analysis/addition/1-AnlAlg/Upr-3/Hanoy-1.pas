   PROGRAM H_a_n_o_y_1;
      Uses CRT;
      type st  = (Left,Middle,Right);
           Nat = 1..MAXINT;
      var  M: Nat;        { M - �᫮ ��᪮� }
   { --------------------------------------- }
   PROCEDURE M_o_v_e (N: Nat; S1,SW,SK: st);
   { ��६�饭�� N ��᪮� � S1 �� SK; }
   { SW - �ᯮ����⥫�� ��থ��    }
   { -------------------------------- }
   PROCEDURE  S_t_e_p;
   { ��६�饭�� ������ ��᪠ � S1 �� SK }
   { ----------------------------------- }
   PROCEDURE P_r_i_n_t (S: st);
   BEGIN
      Case S of
        Left  : Write ('����');
        Middle: Write ('�।���');
        Right : Write ('�ࠢ�')
      end
   END;
  {---- }
   BEGIN
      Write ('����� ��� � '); P_r_i_n_t (S1);
      Write (' ������ �� ');   P_r_i_n_t (SK); WriteLn
   END;
  { --- }
   BEGIN
      If N=1
        then S_t_e_p
        else begin
               M_o_v_e (N-1,S1,SK,SW); S_t_e_p;
               M_o_v_e (N-1,SW,S1,SK)
             end
   END;
  { --- }
   BEGIN
      WriteLn('������ ������⢮ ��᪮�...'); Read (M);
      WriteLn;
      WriteLn('��� ', M:3,
              ' ��᪮� ᫥��� �ந����� ᫥���騥 ����⢨�:');
      M_o_v_e (M,Left,Middle,Right);
      ReadKey
   END.
