   /* ���������� ���஢�� ��⮤�� ���⮣� �롮� */
   /* (���� ᯮᮡ)                                 */
   /* ----------------------------------------------- */
   #include<stdio.h>
   #include<stdlib.h>
   #include<conio.h>
   #include<time.h>
   #define N 6      /* ������⢮ ����⮢ � ���ᨢ� */
      void sortChoice_1 (int *);
      void obmen (int *,int *);
      void print (int *);
  /* ------------------ */
   int main()
   {
      int i,a[N];
      printf("������: 0 - \"��砩��\" ���ᨢ,"
             " 1 - ���� ���ᨢ� � ����������: ");
      scanf("%d",&i);
      if (i)
      {
        printf("������ ���ᨢ �� %u ����⮢:\n",N);
        for (i=0;i<N;i++)
          scanf("%d",&a[i]);
      }
      else {
             srand(time(NULL));
             for (i=0;i<N;i++)
               a[i]=rand()%10;
           }
      printf("��室�� ���ᨢ: "); print(a);
      printf("��蠣���� ���������� ���஢�� ��⮤��"
             " ���⮣� �롮� (���� ᯮᮡ):\n\n");
      sortChoice_1(a);
      printf("\n�������: "); print(a);
      getch();
      return 0;
   }
  /* ---------------------- */
   void sortChoice_1 (int *p)
   /* ����஢�� ��⮤�� ���⮣� �롮� (���� ᯮᮡ) */
   /* -------------------------------------------------- */
   {
      int i,j,k;
      for (i=0;i<N-1;i++)
      {
        k=i;
        for (j=i+1;j<N;j++)
          if (p[j]<p[k])
            k=j;
        if (k!=i)
        {
          obmen(&p[k],&p[i]); print(p);
        }
      }
   }
  /* ---------------------- */
   void obmen (int *x,int *y)
   {
      int klad=*x;
      *x=*y; *y=klad;
   }
  /* --------------- */
   void print (int *p)
   /* �뢮� ����⮢ ���ᨢ� �� �࠭ */
   /* -------------------------------- */
   {
      int i;
      for (i=0;i<N;i++)
        printf("%d ",p[i]);
      printf("\n");
   }
