   /* ���������� ���஢�� ��⮤�� ���⮣� �롮� */
   /* (��ன ᯮᮡ)                                 */
   /* ----------------------------------------------- */
   #include<stdio.h>
   #include<stdlib.h>
   #include<conio.h>
   #include<time.h>
   #define N 7      /* ������⢮ ����⮢ � ���ᨢ� */
     void sortChoice_2 (int *);
     int minI (int,int *);
     void obmen (int *,int *);
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
      printf("��蠣���� ���������� ���஢�� ��⮤�� "
             "���⮣� �롮� (��ன ᯮᮡ):\n");
      sortChoice_2(a);
      printf("�������: "); print(a);
      getch();
      return 0;
   }
  /* ---------------------- */
   void sortChoice_2 (int *p)
   /* ����஢�� ��⮤�� ���⮣� �롮� (��ன ᯮᮡ) */
   /* -------------------------------------------------- */
   {
      int i,j,k;
      for (i=0;i<N-1;i++)
        obmen(&p[minI(i,p)],&p[i]);
   }
  /* ----------------------- */
   int minI (int start,int *p)
   /* �㭪�� ��室�� ��������� ����� "�ࠢ��" start */
   /* (������ start) � �����頥� ��� �����             */
   /* -------------------------------------------------- */
   {
      int m,i;
      for (m=start,i=start+1;i<N;i++)
        if (p[i]<p[m])
          m=i;
      if (m!=start)
        print(p);
      return m;
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
