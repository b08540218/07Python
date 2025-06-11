import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
                       password='1234', db='sample_db', charset='utf8', port=3306)
# 커서 생성
curs = conn.cursor()

def print_menu():
  print("1. 입력")
  print("2. 출력")
  print("3. 검색")
  print("4. 수정")
  print("5. 삭제")
  print("6. 종료")

# 입력
def insert_contact(contact_list):
  print("-----------------------입력기능----------------------------------")
  sql = f"""INSERT INTO phonebook (name, phoneNum, address)
        VALUES ('{input('이름>>>')}','{input('전화번호>>>')}','{input('주소>>>')}')"""



  try:
    curs.execute(sql)
    conn.commit()
    print("레코드가 입력됨")
  except Exception as e:
    conn.rollback()
    print("쿼리 실행시 오류발생", e)
  
  conn.close()

# 수정
def update_contact(contact_list):

  sql = """update phonebook set name ='{1}', phoneNum='{2}', address={3}, where num={0}
""".format(input('수정할일련번호:'), input('이름:'), input('전화번호:'),  input('주소:'))

  try:
    curs.execute(sql)
    conn.commit()
    print("레코드가 입력됨")
  except Exception as e:
    conn.rollback()
    print("쿼리 실행시 오류발생", e)

  conn.close()


  # #삭제
def delete_contact(contact_list):
  while True:
    iStr = input("삭제할 이름 (종료하려면 'exit' 입력): ")
    if iStr.lower() == 'exit':
      print("프로그램을 종료합니다.")
      break

    sql = f"delete from phonebook where name='{iStr}'"
    try:
      curs.execute(sql)
      conn.commit()
      print("1개의 레코드가 삭제됨")
    except Exception as e:
      conn.rollback()
      print("쿼리 실행시 오류발생", e)

  conn.close()

  # def delete_record():

def main():
    contact_list = []
    while True:
        print_menu()
        choice = input("메뉴 선택 (1-6): ")
        if choice == '1':
            insert_contact(contact_list)
        # elif choice == '2':
        #     print_contacts(contact_list)
        # elif choice == '3':
        #     search_contact(contact_list)
        elif choice == '4':
            update_contact(contact_list)
        elif choice == '5':
            delete_contact(contact_list)
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()