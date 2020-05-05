   /* ���������� ࠡ��� � �������筮� �㭪樥� */
   /* qsort(), ॠ�����饩 ������ ����ன  ��- */
   /* �஢�� �.����                             */
   /* ------------------------------------------- */
   #include<stdio.h>
   #include<stdlib.h>
   #include<conio.h>
   #define N 15
      int comp (const void *,const void *);
      int comp1(const void *,const void *);
      int comp2(const void *,const void *);
   /* ---------------------------------- */
   int main()
   {
      int num[N],i;
      /* ------------------------- */
      /* ���� "��砩����" ���ᨢ� */
      /* ------------------------- */
      for (i=0;i<N;i++)
	num[i]=rand()%10;
      printf("��室�� ���ᨢ:\n");
      for (i=0;i<N;i++)
	printf("%d ",num[i]);
      printf("\n\n");
      /* ------------------------ */
      qsort(num,N,sizeof(int),comp);
      printf("������� ���஢�� (�� �����⠭��):\n");
      for (i=0;i<N;i++)
        printf("%d ",num[i]);
      printf("\n\n");
      /* ------------------------- */
      qsort(num,N,sizeof(int),comp1);
      printf("������� ���஢�� (�� �뢠���):\n");
      for (i=0;i<N;i++)
        printf("%d ",num[i]);
      printf("\n\n");
      /* ------------------------- */
      qsort(num,N,sizeof(int),comp2);
      printf("������� ���஢�� (�� �᫮��� x+y>2):\n");
      for (i=0;i<N;i++)
	printf("%d ",num[i]);
      printf("\n\n");
      getch();
      return 0;
   }
   /* -------------------------------- */
   int comp (const void *i,const void *j)
   /* �㭪��, ��������� १���� �ࠢ����� */
   /* 楫�� �ᥫ                               */
   {
     return *(int *)i - *(int *)j;
   }
   /* --------------------------------- */
   int comp1 (const void *i,const void *j)
   /* �㭪��, ��������� १���� �ࠢ����� */
   /* 楫�� �ᥫ                               */
   {
     return *(int *)j - *(int *)i;
   }
   /* --------------------------------- */
   int comp2 (const void *i,const void *j)
   /* �㭪��, ��������� १���� �ࠢ����� */
   /* 楫�� �ᥫ                               */
   {
     return *(int *)i + *(int *)j > 2;
   }
