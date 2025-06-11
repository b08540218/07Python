import pymysql

conn = pymysql.connect(host='localhost',user='sample_user',password='1234',
    db='sample_db',charset='utf8',port=3306
)
curs = conn.cursor()

def print_menu():
    print("\n============= 연락처 관리 프로그램 =============")
    print("1. 입력 | 2. 출력 | 3. 검색 | 4. 수정 | 5. 삭제 | 6. 종료")

# 입력
def input_contact():
    print("\n============= 입력기능 =============")
    name = input("이름>>> ")
    phone = input("전화번호>>> ")
    address = input("주소>>> ")

    sql = f"INSERT INTO phonebooks (name, phoneNum, address) VALUES ('{name}', '{phone}', '{address}')"
    try:
        curs.execute(sql)
        conn.commit()
        print("연락처가 저장되었습니다.")
    except Exception as e:
        conn.rollback()
        print("입력 중 오류 발생:", e)

# 출력
def print_contacts():
    sql = f"SELECT num, name, phoneNum, address FROM phonebooks"
    curs.execute(sql)
    rows = curs.fetchall()

    if not rows:
        print("등록된 연락처가 없습니다.")
        return

    print("\n============= 출력기능 =============")
    for row in rows:
        print(f"{row[0]}. {row[1]} | {row[2]} | {row[3]}")

# 검색
def search_contact():
    print("\n============= 검색기능 =============")
    name = input("검색할 이름>>> ")
    sql = f"SELECT num, name, phoneNum, address FROM phonebooks WHERE name = '{name}'"
    curs.execute(sql)
    rows = curs.fetchall()

    if not rows:
        print("해당 이름의 연락처를 찾을 수 없습니다.")
        return

    for row in rows:
        print(f"{row[0]}. {row[1]} | {row[2]} | {row[3]}")

# 수정
def update_contact():
    print("\n============= 수정기능 =============")
    num = input("수정할 연락처의 번호(num)>>> ")
    name = input("새 이름>>> ")
    phone = input("새 전화번호>>> ")
    address = input("새 주소>>> ")

    sql = f"UPDATE phonebooks SET name='{name}', phoneNum='{phone}', address='{address}' WHERE num='{num}'"
    try:
        curs.execute(sql)
        conn.commit()
        if curs.rowcount:
            print("수정 완료.")
        else:
            print("해당 번호의 연락처가 없습니다.")
    except Exception as e:
        conn.rollback()
        print("수정 중 오류 발생:", e)

# 삭제
def delete_contact():
    print("\n============= 삭제기능 =============")
    num = input("삭제할 연락처의 번호(num)>>> ")
    sql = f"DELETE FROM phonebooks WHERE num = '{num}'"
    try:
        curs.execute(sql)
        conn.commit()
        if curs.rowcount:
            print("삭제 완료.")
        else:
            print("해당 번호의 연락처가 없습니다.")
    except Exception as e:
        conn.rollback()
        print("삭제 중 오류 발생:", e)

def main():
    while True:
        print_menu()
        choice = input("메뉴 선택 (1-6): ")
        if choice == '1':
            input_contact()
        elif choice == '2':
            print_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

    curs.close()
    conn.close()

if __name__ == "__main__":
    main()
