# 데이터베이스 접속 및 커서 생성
import pymysql
import pandas as pd
import os

# DB 연결
conn = pymysql.connect( host = 'localhost',
                        port=3306, # mysql 포트
                        user='root', # 접속 계정
                        password = 'wjdwl7468!', # 루트계정의 본인 비번
                        db = 'testdb',  # 접속하고자 하는 데이타베이스명
                        charset = 'utf8' )
cursor = conn.cursor()
print(cursor)

# 책 목록 보기 함수 정의
def showBook():
    print('='*30)
    print('책 목록 전체 보기')
    print('='*30)
    sql = 'select * from bookTbl;'
    cursor.execute(sql)
    bookdata = cursor.fetchall()
    for row in bookdata:
        print(row)


# 책 추가 함수 정의
def insertBook():
    print('='*30)
    print('레코드 삽입하기')
    print('='*30)
    bookname1 = input('책이름=> ' ).strip()
    writer1 = input('저자=> ' ).strip()
    page1 = input('페이지수=> ' ).strip()
    price1 = input('가격=> ' ).strip()
    total = (bookname1, writer1, page1, price1)
    sql = '''INSERT INTO bookTbl (title, writer, page, price) VALUES (%s, %s, %s, %s);'''
    cursor.execute(sql, total)
    conn.commit()


# 책 수정 함수 정의
def updateBook():
    renum = input('수정할 책 번호는?=> ' ).strip()
    print('='*30)
    recon = input('수정 사항 선택? (1.책제목  2.저자  3.페이지수  4.가격)=> ' ).strip()
    print('='*30)
    if recon == '1':
        sql1 = 'UPDATE bookTbl SET title = %s WHERE id = %s;'
        rename = input('책제목을 입력하세요 => ' ).strip()
        cursor.execute(sql1,(rename, renum))
        conn.commit()   
    elif recon == '2':
        sql2 = 'UPDATE bookTbl SET writer = %s WHERE id = %s;'
        rewriter = input('저자를 입력하세요 => ' ).strip()
        cursor.execute(sql2,(rewriter, renum))
        conn.commit()  
    elif recon == '3':
        sql3 = 'UPDATE bookTbl SET page = %s WHERE id = %s;'
        repage = input('페이지를 입력하세요 => ' ).strip()
        cursor.execute(sql3,(repage, renum))
        conn.commit()  
    elif recon == '4':
        sql4 = 'UPDATE bookTbl SET price = % WHERE id = %s;'
        reprice = input('가격을 입력하세요 => ' ).strip()
        cursor.execute(sql4,(reprice,renum))
        conn.commit() 
    else:
        print('입력오류 발생')


# 책 삭제 함수 정의
def delBook():
    delnum = input('삭제할 책 번호는?=> ' ).strip()
    print('='*30)    
    sql ="DELETE FROM bookTbl WHERE id = %s"
    cursor.execute(sql, (delnum,))
    conn.commit()
    


# 도서정보 메뉴 
while(True):
    print('1.목록보기  2.추가  3.수정  4.삭제  0.종료')
    # 메뉴입력받기
    choice = input('=> ' ).strip()
    if choice == '1':
        # print('목록보기 출력 예정')
        showBook()
    elif choice == '2':
        # print('레코드 추가 예정')
        insertBook()
    elif choice == '3':
        # print('레코드 수정 예정')
        showBook()
        updateBook()
        print('데이터가 수정되었습니다.')
    elif choice == '4':
        # print('레코드 삭제 예정')
        showBook()
        delBook()
        print('데이터가 삭제되었습니다.')
    elif choice == '0':
        print('프로그램 종료')
        break
    else:
        print('입력 오류 발생')


conn.close()