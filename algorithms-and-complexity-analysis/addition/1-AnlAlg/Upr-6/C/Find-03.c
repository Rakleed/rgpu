   /* ����������:                                          */
   /*                                                        */
   /*  (1) ����୮�� ���᪠ ������ ��������� ������� ����- */
   /*      ��୮�� �᫮���� ���ᨢ�, 㯮�冷祭���� �� ���- */
   /*      ��⠭�� (४��ᨢ�� ��ਠ��);                   */
   /*                                                        */
   /*  (2) ��।������ �६��� �믮������ �ணࠬ��          */
   /* ------------------------------------------------------ */
   #include<stdio.h>
   #include<stdlib.h>
   #include<time.h>
   #define N 100         /* ������⢮ ������⮢ � ���ᨢ� */
      int binSearch(int *,int,int,int);
      void bubbleSort(int *);
      void obmen(int *,int *);
  /* ----------------------- */
   int main()
   {
      int a[N],          /* ��室�� ���ᨢ */
          i,             /* ��ࠬ��� 横��� */
          x;             /* �᪮�� ������� */
      clock_t start,end;
      /* ----------------------------------------------- */
      printf("���������� ���ᨢ� ��砩�묨 �᫠��...\n");
      srand(time(NULL));
      for (i=0;i<N;i++)
        a[i]=rand()%10;
      /* ----------------------------- */
      /* ����஢�� ����񭭮�� ���ᨢ� */
      /* ----------------------------- */
      bubbleSort(a);
      /* ------------------------- */
      /* ����஫�� �뢮� ���ᨢ� */
      /* ------------------------- */
      printf("������ ���ᨢ: ");
      for (i=0;i<N;i++)
        printf("%u ",a[i]);
      /* ---------------------------------------- */
      printf("\n�᪮�� �������: "); scanf("%u",&x);
      start=clock();
      i=binSearch(a,0,N-1,x);
      end=clock();
      printf("�६� ࠡ��� �ணࠬ��: %6.6f ᥪ\n",
                  (double)(end-start)/(double)CLOCKS_PER_SEC);
      if (i!=-1)
      {
        printf("������� ������; ���� �� ��� ����஢: %u\n",i);
        int j=i;
        while (a[i]==a[--i]);
        while (a[j]==a[++j]);
        printf("�������� �����ᮢ �᪮���� �������: (%d,%d)\n",
               ++i,--j);
      }
      else printf("������� �� ������.\n");
      system("pause");
      return 0;
   }
  /* ------------------------------------------ */
   int binSearch(int *arr,int low,int high,int y)
   {
      int mid;      /* "�।���" ������ ������⮢ ���ᨢ� */
      /* ------------------------------------------------ */
      if (low>high)
        return -1;
      else if (y==*(arr+(mid=(low+high)/3)))
             return mid;
           else if (y<*(arr+mid))
                  return binSearch(arr,low,mid-1,y);
                else return binSearch(arr,mid+1,high,y);
   }
  /* ------------------- */
   void bubbleSort(int *p)
   /* ����஢�� ��⮤�� ���⮣� ������ */
   /* ---------------------------------- */
   {
      int i,j;
      for (i=0;i<N;i++)
        for (j=N-1;j>i;j--)
          if (p[j-1]>p[j])
            obmen(&p[j-1],&p[j]);
   }
  /* --------------------- */
   void obmen(int *x,int *y)
   {
      int klad=*x;
      /* --------- */
      *x=*y; *y=klad;
   }
