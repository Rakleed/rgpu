   -- ���������� �㭪樨, ������饩  � � � � � � � �
   -- �।�� ����                            
   --                                                 
   --   lim  f(x)=b=?                                 
   --   x->x0      
   --
   -- eps    - �筮���, �ᯮ��㥬�� � ���ਨ ���;
   -- x1, x2 - �窨 �� ������ ��।������ �㭪樨 y=f(x);
   -- x0     - �।��쭠� �窠 (�窠 �ਪ�᭮�����)
   --
   -- ����: �.�.���檨� (30.05.2018)
   -- *******************************
   lim f x0 x1 x2 eps
        | abs (f x1-f x2)<eps = (f x1+f x2)/2.0
        | True                = lim f x0 ((x0+x1)/2.0) ((x0+x2)/2.0) eps

   -- ***************************
   -- ��㤠�� ��⮢� �ਬ���:
   -----------------------------------------
   test = lim f x0 (x0-eps1) (x0+eps1) 0.001
      where 
            x0  = 0.0
         -- x0  = 1.0
            eps1= 0.5
                  -- ����稭� eps1 �롨ࠥ��� ������᪨...
            f   = -- \x -> (exp(7*x)-exp(-2*x)) / (sin(x)-2*x)
                                                  -- -9.0
                  -- \x -> x*x*sin (1.0/x)           
                                                  -- 0.0           
                  -- \x -> ((logBase 10.0 (1+x))/6/x) ** (x/(x+2.0))
                                                  -- 1.0
                  -- \x -> (3**(5*x-3)-3**(2*x*x)) / tan(pi*x)
                                                  -- 0
                  -- \x -> (3**(5.0*x)-3**(2.0*x*x)) / tan(pi*x)
                                                  -- 5.493/pi=1.74851
                  -- \x -> 1/x/x - 1/tan(x)/tan(x)      
                                                  -- 2.0/3.0=0.(6)
                     \x -> (1.0/x)*(31**x-1)      -- ln(31)=3.43399