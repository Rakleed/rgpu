   /* ���������� ࠡ��� � �������筮� �㭪樥� qsort(), */
   /* ॠ�����饩 ������ ����ன ���஢�� �.����      */
   /* ---------------------------------------------------- */
   #include<stdio.h>
   #include<stdlib.h>
   #include<string.h>
   #include<conio.h>
      int comp (const void *,const void *);
   /* ---------------------------------- */
   int main()
   {
      char num[100];
      int i,N;
      printf("������ ��ਭ�      : "); gets(num);
      N=strlen(num);
      qsort(num,N,sizeof(char),comp);
      printf("������� ���஢��: "); puts(num);
      printf("\n");
      getch();
      return 0;
   }
  /* ---------------------------------- */
   int comp (const void *i,const void *j)
   /* �㭪��, ��������� १���� �ࠢ����� */
   /* 楫�� �ᥫ                               */
   {
     return *(char *)i - *(char *)j;
   }
