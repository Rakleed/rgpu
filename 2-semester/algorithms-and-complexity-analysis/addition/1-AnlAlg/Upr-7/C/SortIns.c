   /* ���������� ���஢�� ����묨 ����祭�ﬨ */
   /* -------------------------------------------- */
   #include<stdio.h>
   #include<stdlib.h>
   #include<conio.h>
   #include<time.h>
   #define N 5          /* ������⢮ ����⮢ � ���ᨢ� */
     void sortInsert (int *);
     void print (int *);
  /* ----------------- */
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
      printf("��蠣���� ���������� ���஢�� "
             "����묨 ����祭�ﬨ:\n");
      sortInsert(a);
      printf("�������: "); print(a);
      getch();
      return 0;
   }
  /* -------------------- */
   void sortInsert (int *p)
   /* ����஢�� ����묨 ����祭�ﬨ */
   /* ------------------------------- */
   {
      int i,j,x;
      for (i=1;i<N;i++)
      {
        x=p[i];
        for (j=i-1;j>=0&&x<p[j];j--)
          p[j+1]=p[j];
        p[j+1]=x;
        print(p);
      }
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
