def print_menu():
    print("\n[ 연락처 관리 메뉴 ]")
    print("1. 입력 | 2. 출력 | 3. 검색 | 4. 수정 | 5. 삭제 | 6. 종료")


def input_contact(contact_list):
    name = input("성명: ")
    phone = input("전화번호: ")
    address = input("주소: ")
    contact_list.append({"name": name, "phone": phone, "address": address})
    print(f"입력 완료: {name} | {phone} | {address}")

def print_contacts(contact_list):
    if not contact_list:
        print(f"\n등록된 연락처가 없습니다.")
        return
    print(f"\n[전체 연락처] ({len(contact_list)}건)")
    for i, contact in enumerate(contact_list, 1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['address']}")

def search_contact(contact_list):
    keyword = input("검색할 이름: ")
    found = False
    for contact in contact_list:
        if contact['name'] == keyword:
            print(f"찾음: {contact['name']} | {contact['phone']} | {contact['address']}")
            found = True
            break
    if not found:
        print(f"'{keyword}' 이름의 연락처를 찾을 수 없습니다.")

def update_contact(contact_list):
    keyword = input("수정할 이름: ")
    for contact in contact_list:
        if contact['name'] == keyword:
            print(f"기존 정보: {contact['name']} | {contact['phone']} | {contact['address']}")
            new_phone = input("새 전화번호: ")
            new_address = input("새 주소: ")
            contact['phone'] = new_phone
            contact['address'] = new_address
            print(f"수정 완료: {contact['name']} | {contact['phone']} | {contact['address']}")
            return
    print(f"'{keyword}' 이름의 연락처를 찾을 수 없습니다.")

def delete_contact(contact_list):
    keyword = input("삭제할 이름: ")
    for i, contact in enumerate(contact_list):
        if contact['name'] == keyword:
            del contact_list[i]
            print(f"'{keyword}' 연락처가 삭제되었습니다.")
            return
    print(f"'{keyword}' 이름의 연락처를 찾을 수 없습니다.")

def main():
    contact_list = []
    while True:
        print_menu()
        choice = input("메뉴 선택 (1-6): ")
        if choice == '1':
            input_contact(contact_list)
        elif choice == '2':
            print_contacts(contact_list)
        elif choice == '3':
            search_contact(contact_list)
        elif choice == '4':
            update_contact(contact_list)
        elif choice == '5':
            delete_contact(contact_list)
        elif choice == '6':
            print(f"프로그램을 종료합니다.")
            break
        else:
            print(f"잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
