   /* ��������� �����⬠ ���஢�� ᫨ﭨ�� */
   /* ---------------------------------------- */
   #include<stdio.h>
   #include<conio.h>
   #define N 7
      void mergeSort (int*,int,int);
      void mergeList (int*,int,int,int,int);
   /* ----------------------------------- */
   int main()
   {
      int i,m[N];
      printf("������ %d 楫�� �ᥫ   : ",N);
      for (i=0; i<N; i++)
        scanf("%d",&m[i]);
      /* -------------------------------- */
      printf("����஫�� �뢮� ���ᨢ�: ");
      for (i=0; i<N; i++)
        printf("%d ",m[i]);
      /* ------------------------------------------ */
      printf("\n�������    : "); mergeSort(m,0,N-1);
      for (i=0; i<N; i++)
        printf("%d ",m[i]);
      printf("\n");
      getch();
      return 0;
   }
   /* ----------------------------- */
   void mergeSort (int* a,int l,int r)
   {
     if (l<r)
     {
       mergeSort(a,l,(l+r)/2);
       mergeSort(a,(l+r)/2+1,r);
       mergeList(a,l,(l+r)/2,(l+r)/2+1,r);
     }
   }
  /* ---------------------------------------------- */
   void mergeList (int* a,int l1,int r1,int l2,int r2)
   {
     int temp[N],l=l1,i;
     for (i=l; l1<=r1 && l2<=r2; i++)
       if (a[l1]<a[l2])
         temp[i]=a[l1++];
       else temp[i]=a[l2++];
     /* --------------------------------- */
     /* ��७�� ��⠢襩�� ��� "ᯨ᪠" */
     /* --------------------------------- */
     if (l1<=r1)
       for (; l1<=r1; i++, l1++)
         temp[i]=a[l1];
     else for (; l2<=r2; i++, l2++)
            temp[i]=a[l2];
     /* --------------------------------- */
     /* �����饭�� १���� � ���ᨢ a */
     /* --------------------------------- */
     for (i=l;i<=r2;i++)
       a[i]=temp[i];
   }
