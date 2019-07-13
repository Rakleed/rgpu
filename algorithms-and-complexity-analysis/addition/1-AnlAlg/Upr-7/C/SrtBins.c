   /* ���������� ���஢�� �����묨 ����祭�ﬨ */
   /* --------------------------------------------- */
   #include<stdio.h>
   #include<stdlib.h>
   #include<conio.h>
   #include<time.h>
   #define N 9                /* ������⢮ ����⮢ � ���ᨢ� */
     void sortBinInsert (int *);
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
             "�����묨 ����祭�ﬨ:\n");
      sortBinInsert(a);
      printf("\n�������: "); print(a);
      getch();
      return 0;
   }
  /* ----------------------- */
   void sortBinInsert (int *p)
   /* ����஢�� �����묨 ����祭�ﬨ */
   /* -------------------------------- */
   {
      int i,j,   /* ��ࠬ���� 横���                  */
          x,     /* �ᯮ����⥫쭠� ��६�����        */
          m,     /* "��।���" �஬���⪠             */
          l,r;   /* ����� � �ࠢ�� �࠭��� �஬���⪠ */
      /* -------------------------------------------- */
      for (i=1;i<N;i++)
      {
        x=p[i]; l=0; r=i-1;
        while (l<=r)
          if (x<p[m=(l+r)/2])
            r=m-1;
          else l=m+1;
        for (j=i-1;j>=l;j--)
          p[j+1]=p[j];
        p[l]=x;
        print(p);
      }
   }
  /* --------------- */
   void print (int *p)
   /* �뢮� ����⮢ ���ᨢ� �� �࠭ */
   /* -------------------------------- */
   {
      int i;
      /* ----------- */
      for (i=0;i<N;i++)
        printf("%d ",p[i]);
      printf("\n");
   }
