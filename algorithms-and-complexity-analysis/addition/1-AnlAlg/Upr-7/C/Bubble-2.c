   /* ���������� ���஢�� ��⮤�� ���⮣� ������ */
   /* (��ன ᯮᮡ)                                 */
   /* ----------------------------------------------- */
   #include<stdio.h>
   #include<stdlib.h>
   #include<conio.h>
   #include<time.h>
   #define N 5      /* ������⢮ ����⮢ � ���ᨢ� */
      int f;
      void bubbleSort2(int *);
      void obmen(int *,int *);
      void print(int *);
   /* --------------- */
   int main()
   {
      int i,a[N];
      /* ------------------------------------- */
      printf("������: 0 - \"��砩��\" ���ᨢ,"
             " 1 - ���� ���ᨢ� � ����������: ");
      scanf("%d",&i);
      if (i)
      {
        printf("������ ���ᨢ �� %u ����⮢:\n",N);
        for (i=0; i<N; i++)
          scanf("%d",&a[i]);
      }
      else {
             srand(time(NULL));
             for (i=0; i<N; i++)
               a[i]=rand()%10;
           }
      printf("����஫�� �뢮� ��室���� ���ᨢ�: "); print(a);
      printf("��蠣���� ���������� ���஢�� ��⮤��\n"
             "���⮣� ������ (��ன ᯮᮡ):\n");
      bubbleSort2(a);
      printf("�������: "); print(a);
      getch();
      return 0;
   }
   /* ---------------------------------- */
   /* ����஢�� ��⮤�� ���⮣� ������ */
   /* (��ன ��ਠ��)                   */
   /* ---------------------------------- */
   void bubbleSort2 (int *p)
   {
      int i,j; /* ��ࠬ���� 横���                    */
               /* �᫨ �� �����, � f=1, ���� - f=0 */
      for (f=1,i=0; i<N&&f; i++)
        for (f=0,j=N-1; j>i; j--)
          if (p[j-1]>p[j])
          {
            f=1; obmen(&p[j-1],&p[j]); print(p);
          }
   }
  /* --------------------- */
   void obmen(int *x,int *y)
   {
      int klad=*x;
      *x=*y; *y=klad;
   }
   /* ----------------------- */
   /* �뢮� ����⮢ ���ᨢ� */
   /* ----------------------- */
   void print (int *p)
   {
      int i;
      for (i=0; i<N; i++)
        printf("%d ",p[i]);
      printf("\nf = %d",f);
      printf("\n\n");
   }
