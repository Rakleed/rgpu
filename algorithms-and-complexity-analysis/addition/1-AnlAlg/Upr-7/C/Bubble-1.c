   /* ���������� ���஢�� ��⮤�� ���⮣� ������ */
   /* (���� ᯮᮡ)                                 */
   /* ----------------------------------------------- */
   #include<stdio.h>
   #include<stdlib.h>
   #include<conio.h>
   #include<time.h>
   #define N 5        /* ������⢮ ����⮢ � ���ᨢ� */
      void bubbleSort1 (int *);
      void obmen (int *,int *);
      void print (int *);
   /* ---------------- */
   int main()
   {
      int i,a[N];
      /* ------------------------------------- */
      printf("������: 0 - \"��砩��\" ���ᨢ,"
             " 1 - ���� ���ᨢ� � ����������: ");
      scanf("%d",&i);
      if (i)
      {
        /* ���� ���ᨢ� � ���������� */
        printf("������ ���ᨢ �� %u ����⮢:\n",N);
        for (i=0; i<N; i++)
          scanf("%d",&a[i]);
      }
      else {
             /* ���砩�� ���� ���ᨢ� */
             srand(time(NULL));
             for (i=0; i<N; i++)
               a[i]=rand()%10;
           }
      printf("����஫�� �뢮� ��室���� ���ᨢ�: "); print(a);
      printf("��蠣���� ���������� ���஢�� ��⮤��\n"
             "���⮣� ������ (���� ᯮᮡ):\n");
      bubbleSort1(a);
      printf("�������: "); print(a);
      getch();
      return 0;
   }
   /* ---------------------------------- */
   /* ����஢�� ��⮤�� ���⮣� ������ */
   /* (���� ��ਠ��)                   */
   /* ---------------------------------- */
   void bubbleSort1 (int *p)
   {
      int i,j;
      for (i=0; i<N; i++)
        for (j=N-1; j>i; j--)
          if (p[j-1]>p[j])
          {
            obmen(&p[j-1],&p[j]); print(p);
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
      printf("\n");
   }
