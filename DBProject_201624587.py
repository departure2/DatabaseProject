import psycopg2
import sys
import time
from datetime import datetime
from prettytable import PrettyTable

if __name__ == '__main__':
    con = psycopg2.connect(
        database='dbtermproject',
        user='db2023',
        password='db!2023',
        host='::1',
        port='5432'
    )

# 데이터베이스를 탐색 후, 다음 primary key로 이용되는 id 값을 지정
def get_next_p_id():
    cursor = con.cursor()
    cursor.execute("SELECT MAX(p_id) FROM patient")
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1 if result is not None else 1
def get_next_d_id():
    cursor = con.cursor()
    cursor.execute("SELECT MAX(d_id) FROM disease")
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1 if result is not None else 1
def get_next_m_id():
    cursor = con.cursor()
    cursor.execute("SELECT MAX(m_id) FROM medicine")
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1 if result is not None else 1
def get_next_c_id():
    cursor = con.cursor()
    cursor.execute("SELECT MAX(c_id) FROM counselor")
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1 if result is not None else 1
def get_next_j_id():
    cursor = con.cursor()
    cursor.execute("SELECT MAX(j_id) FROM journalist")
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1 if result is not None else 1
def get_next_t_id():
    cursor = con.cursor()
    cursor.execute("SELECT MAX(t_id) FROM counsel_table")
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1 if result is not None else 1
def get_next_w_id():
    cursor = con.cursor()
    cursor.execute("SELECT MAX(w_id) FROM writing")
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1 if result is not None else 1
def get_next_r_id():
    cursor = con.cursor()
    cursor.execute("SELECT MAX(r_id) FROM requested_writing")
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1 if result is not None else 1
def get_next_n_id():
    cursor = con.cursor()
    cursor.execute("SELECT MAX(n_id) FROM notification")
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1 if result is not None else 1

p_id, d_id, m_id, c_id, j_id, t_id, w_id, r_id, n_id \
    = get_next_p_id(), get_next_d_id(), get_next_m_id(), get_next_c_id(), get_next_j_id(), get_next_t_id(), get_next_w_id(), get_next_r_id(), get_next_n_id()

# 시작 화면
def initial():
    print("\n*****만성질환자 관리를 부탁해! '만관부' 어플리케이션입니다.*****\n")
    time.sleep(0.5)
    print("만관부 실행중...\n")
    time.sleep(1)
    print("환영합니다!")
    time.sleep(1)
    initial_choice()
# 초기 선택창
def initial_choice():
    global p_id, d_id, m_id, c_id, j_id, t_id, w_id, r_id
    p_id, d_id, m_id, c_id, j_id, t_id, w_id, r_id \
        = get_next_p_id(), get_next_d_id(), get_next_m_id(), get_next_c_id(), get_next_j_id(), get_next_t_id(), get_next_w_id(), get_next_r_id()
    choice = input("\n원하는 서비스에 해당하는 숫자를 입력해 주세요.\n1. 회원가입\n2. 로그인\n3. 어플리케이션 종료\n")
    if (choice == "1"):
        sign_up()
    elif (choice == "2"):
        login()
    elif (choice == "3"):
        print("\n어플리케이션을 종료하려면 'EXIT'을 입력해 주세요. 종료를 원치 않는다면 다른 문자를 아무거나 입력해 주세요: ")
        isexit = input()
        if isexit.upper() == "EXIT":
            print("---어플리케이션을 종료합니다.---")
            sys.exit()
        else:
            print("\n---어플리케이션을 종료하지 않습니다.---")
            time.sleep(0.5)
            initial_choice()
    else:
        print("\n올바른 입력이 아닙니다. 숫자 1~3 중 하나를 입력해 주세요.")
        time.sleep(0.5)
        initial_choice()

#회원가입
def sign_up():
    print("\n---회원가입을 진행합니다.---\n")
    role_num = input("이용자 유형을 선택해 주세요. \n1. 만성질환자\n2. 건강상담사\n3. 기자\n4. 뒤로가기\n")
    if (role_num == "1"):
        patient_sign_up()
    elif (role_num == "2"):
        counselor_sign_up()
    elif (role_num == "3"):
        journalist_sign_up()
    elif (role_num == "4"):
        initial_choice()
    else:
        print("\n올바른 입력이 아닙니다. 숫자 1~4 중 하나를 입력해 주세요.")
        time.sleep(0.5)
        sign_up()

def patient_sign_up():
    global p_id
    global d_id
    global m_id
    print("\n---만성질환자 가입을 시작합니다. 아래의 정보를 입력해 주세요.---\n")
    id = ID_input()
    pw = PW_input()
    name, pn = NP_input()
    nickname = NNAME_input()
    disease_list = DISEASE_input()
    medicine_list = MEDICINE_input()

    cursor = con.cursor()

    cursor.execute("INSERT INTO patient (p_id, id, password, name, phonenumber, nickname) VALUES (%s, %s, %s, %s, %s, %s)", (p_id, id, pw, name, pn, nickname))

    for disease_name in disease_list:
        cursor.execute("INSERT INTO disease (d_id, p_id, disease_name) VALUES (%s, %s, %s)", (d_id, p_id, disease_name))
        d_id += 1

    for medicine_name in medicine_list:
        cursor.execute("INSERT INTO medicine (m_id, p_id, medicine_name) VALUES (%s, %s, %s)", (m_id, p_id, medicine_name))
        m_id += 1

    con.commit()
    p_id += 1

    print("---만성질환자 가입이 완료되었습니다.---")

    initial_choice()
def counselor_sign_up():
    global c_id

    print("\n---건강상담사 가입을 시작합니다. 아래의 정보를 입력해 주세요.---\n")
    id = ID_input()
    pw = PW_input()
    name, pn = NP_input()

    cursor = con.cursor()

    cursor.execute(
        "INSERT INTO counselor (c_id, id, password, name, phonenumber) VALUES (%s, %s, %s, %s, %s)",
        (c_id, id, pw, name, pn))

    con.commit()
    c_id += 1

    print("---건강상담사 가입이 완료되었습니다.---")

    initial_choice()
def journalist_sign_up():
    global j_id
    print("\n---기자 가입을 시작합니다. 아래의 정보를 입력해 주세요.---\n")
    id = ID_input()
    pw = PW_input()
    name, pn = NP_input()

    cursor = con.cursor()

    cursor.execute(
        "INSERT INTO journalist (j_id, id, password, name, phonenumber) VALUES (%s, %s, %s, %s, %s)",
        (j_id, id, pw, name, pn))

    con.commit()
    j_id += 1

    print("---기자 가입이 완료되었습니다.---")

    initial_choice()
# 회원 가입 시 정보 입력
def ID_input():
    while True:
        id = input("ID(12자 이하): ")

        cursor = con.cursor()
        cursor.execute("SELECT id FROM patient WHERE id = %s", (id,))
        existing_pid = cursor.fetchone()
        cursor.execute("SELECT id FROM counselor WHERE id = %s", (id,))
        existing_cid = cursor.fetchone()
        cursor.execute("SELECT id FROM journalist WHERE id = %s", (id,))
        existing_jid = cursor.fetchone()

        if(len(id) > 12):
            print("12자 이하로 다시 입력해 주세요.\n")
        elif(existing_pid or existing_cid or existing_jid):
            print("이미 존재하는 ID입니다. 다시 입력해 주세요.\n")
        elif(id.upper() == "EXIT"):
            print("부적절한 ID입니다. 다시 입력해 주세요.\n")
        else:
            return id
def PW_input():
    while True:
        pw = input("PW(16자 이하): ")
        if(len(pw) > 16):
            print("16자 이하로 다시 입력해 주세요.\n")
        else:
            return pw
def NAME_input():
    while True:
        name = input("이름(20자 이하): ")
        if(len(name) > 20):
            print("20자 이하로 다시 입력해 주세요.\n")
        else:
            return name
def NP_input():
    only_pn = 0
    while True:
        if(only_pn == 0):
            name = NAME_input()
        pn = input("전화번호(12자 이하의 숫자, - 제외): ")

        cursor = con.cursor()
        cursor.execute("SELECT name, phonenumber FROM patient")
        existing_patient_data = cursor.fetchall()
        cursor.execute("SELECT name, phonenumber FROM counselor")
        existing_counselor_data = cursor.fetchall()
        cursor.execute("SELECT name, phonenumber FROM journalist")
        existing_journalist_data = cursor.fetchall()

        if (name, pn) in existing_patient_data or (name, pn) in existing_counselor_data or (name, pn) in existing_journalist_data:
            print("이미 존재하는 이름과 전화번호 입니다. 다시 입력해 주세요.")
        elif len(pn) > 12:
            print("12자 이하로 입력해 주세요.")
            only_pn = 1
        else:
            try:
                number = int(pn)
                return name, pn
            except ValueError:
                print("숫자만을 입력해 주세요.")
                only_pn = 1
def NNAME_input():
    while True:
        nickname = input("닉네임(12자 이하): ")

        cursor = con.cursor()
        cursor.execute("SELECT nickname FROM patient WHERE nickname = %s", (nickname,))
        existing_nickname = cursor.fetchone()
        if(len(nickname) > 12):
            print("12자 이하로 다시 입력해 주세요.\n")
        elif(existing_nickname):
            print("이미 존재하는 닉네임입니다. 다시 입력해 주세요.\n")
        else:
            return nickname
def DISEASE_input():
    disease_list = []
    print("앓고 있는 질환들을 입력해 주세요. (엔터로 구분, 모두 입력 했다면 'END'를 입력):")
    while True:
        user_input = input()
        if user_input.upper() == "END":
            return disease_list
        disease_list.append(user_input)
def MEDICINE_input():
    medicine_list = []
    print("복용 중인 약들을 입력해 주세요. (엔터로 구분, 모두 입력 했다면 'END'를 입력):")
    while True:
        user_input = input()
        if user_input.upper() == "END":
            return medicine_list
        medicine_list.append(user_input)

# 로그인
global user_information
global disease_information
global medicine_information
def login():
    global user_information
    global disease_information
    global medicine_information
    print("\n---로그인을 진행합니다. 로그인을 취소하려면 ID에 'EXIT'를 입력해 주세요.---\n")
    while True:
        id = input("ID: ")
        if (id.upper() == "EXIT"):
            initial_choice()
            break
        pw = input("PASSWORD: ")

        cursor = con.cursor()
        cursor.execute("SELECT id, password FROM patient")
        existing_patient_data = cursor.fetchall()
        cursor.execute("SELECT id, password FROM counselor")
        existing_counselor_data = cursor.fetchall()
        cursor.execute("SELECT id, password FROM journalist")
        existing_journalist_data = cursor.fetchall()

        if (id, pw) in existing_patient_data:
            print("\n---'만성질환자' 계정 로그인 완료---\n")
            cursor.execute("SELECT * FROM patient WHERE (id, password) = (%s, %s)", (id, pw))
            user_information = cursor.fetchone()
            cursor.execute("SELECT disease_name FROM disease WHERE p_id = %s", (user_information[0],))
            disease_information = cursor.fetchall()
            cursor.execute("SELECT medicine_name FROM medicine WHERE p_id = %s", (user_information[0],))
            medicine_information = cursor.fetchall()
            print('%s님, 반갑습니다!' % user_information[3])
            time.sleep(0.5)
            patient_main()
            return
        elif (id, pw) in existing_counselor_data:
            print("\n---'건강상담사' 계정 로그인 완료---\n")
            cursor.execute("SELECT * FROM counselor WHERE (id, password) = (%s, %s)", (id, pw))
            user_information = cursor.fetchone()
            print('%s님, 반갑습니다!' % user_information[3])
            time.sleep(0.5)
            counselor_main()
            return
        elif (id, pw) in existing_journalist_data:
            print("\n---'기자' 계정 로그인 완료---\n")
            cursor.execute("SELECT * FROM journalist WHERE (id, password) = (%s, %s)", (id, pw))
            user_information = cursor.fetchone()
            print('%s님, 반갑습니다!' % user_information[3])
            time.sleep(0.5)
            journalist_main()
            return
        else:
            print("로그인 정보가 올바르지 않습니다. 다시 입력해 주세요.\n")

def patient_main():
    while True:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM notification WHERE p_id = %s", (user_information[0],))
        existing_notify = cursor.fetchone()
        if(existing_notify):
            print("\n현재 읽지 않은 알림이 존재합니다!")
        choice = input("\n원하는 서비스에 해당하는 숫자를 입력해 주세요.\n1. 건강 상담 조회 및 신청 / 신청된 상담 조회 및 취소\n2. 만성질환 기사 목록 조회\n"
                       "3. 만성질환 기사 요청 / 조회 및 취소\n4. 알림 읽기\n5. 로그아웃\n6. 개인 정보 조회 및 수정\n7. 회원 탈퇴\n")
        if(choice == "1"):
            patient_counsel_choice()
        elif(choice == "2"):
            read_writing()
        elif(choice == "3"):
            request_writing_choice()
        elif(choice == "4"):
            read_notification()
        elif(choice == "5"):
            patient_logout()
        elif(choice == "6"):
            patient_modify()
        elif(choice == "7"):
            patient_sign_out()
        else:
            print("\n올바른 입력이 아닙니다. 숫자 1~7 중 하나를 입력해 주세요.\n")
def patient_counsel_choice():
    while True:
        choice = input("\n원하는 서비스에 해당하는 숫자를 입력해 주세요.\n1. 건강 상담 조회 및 신청\n2. 신청된 상담 조회 및 취소\n3. 뒤로가기\n")
        if(choice == "1"):
            registering_counsel()
            return
        elif(choice == "2"):
            registered_counsel()
            return
        elif (choice == "3"):
            patient_main()
            return
        else:
            print("\n올바른 입력이 아닙니다. 숫자 1~3 중 하나를 입력해 주세요.\n")
def registering_counsel():
    global n_id
    print("\n---예약 가능한 건강 상담 목록을 조회합니다. 희망하는 조건이 없다면 공백으로 답변해 주세요.---\n")
    while True:
        try:
            name_condition = input("건강 상담사의 이름(부분 검색): ")
            date_condition = input("상담 날짜(YYYY-MM-DD 형식): ")
            stime_condition = input("상담 시작 시간 (HH:MM 형식): ")
            etime_condition = input("상담 종료 시간 (HH:MM 형식): ")

            stime_condition += ":00" if stime_condition else ""
            etime_condition += ":00" if etime_condition else ""

            cursor = con.cursor()

            query = "SELECT * FROM counsel_table WHERE (c_name LIKE %s) AND (status = 'Unoccupied')"
            params = [f"%{name_condition}%"]

            if date_condition:
                datetime.strptime(date_condition, '%Y-%m-%d')
                query += " AND (date = %s)"
                params.append(date_condition)
            if stime_condition:
                datetime.strptime(stime_condition, '%H:%M:%S')
                query += " AND (s_time >= %s)"
                params.append(stime_condition)
            if etime_condition:
                datetime.strptime(etime_condition, '%H:%M:%S')
                query += " AND (e_time <= %s)"
                params.append(etime_condition)

            cursor.execute(query, params)

            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            table.add_rows(rows)

            if (rows):
                print(table)
                select = input("\n상담을 원하는 테이블의 t_id를 입력해주세요. 상담 예약을 원치 않으시면 'EXIT'를 입력해주세요: ")
                if select.strip():
                    if (select.upper() != "EXIT"):
                        cursor.execute("SELECT * FROM counsel_table WHERE t_id = %s", (select,))
                        existing_tid = cursor.fetchone()
                        if (existing_tid):
                            cursor.execute("UPDATE counsel_table SET status = 'Occupied', p_id = %s WHERE t_id = %s",
                                           (user_information[0], select))
                            con.commit()
                            print("\n---상담이 예약되었습니다.---\n")
                            con.cursor()
                            cursor.execute("SELECT date FROM counsel_table WHERE t_id = %s", (select,))
                            date = cursor.fetchone()
                            cursor.execute("SELECT s_time FROM counsel_table WHERE t_id = %s", (select,))
                            s_time = cursor.fetchone()
                            cursor.execute("SELECT e_time FROM counsel_table WHERE t_id = %s", (select,))
                            e_time = cursor.fetchone()
                            cursor.execute("INSERT INTO notification (n_id, p_id, message) VALUES (%s, %s, %s)",
                                           (n_id, user_information[0], f'요청하신 날짜 {date}의 {s_time} ~ {e_time} 시간대의 상담이 예약되었습니다.'))
                            con.commit()
                            n_id += 1
                            time.sleep(0.5)
                        else:
                            print("\n올바른 t_id를 입력해 주세요.\n")
                            registering_counsel()
                    else:
                        print("\n---상담 예약을 진행하지 않습니다.---\n")
                        time.sleep(0.5)
                        patient_main()
                else:
                    print("\n올바른 t_id를 입력해 주세요.\n")
                    registering_counsel()
            else:
                print("\n---조건에 맞는 상담 테이블이 없습니다.---\n")
                time.sleep(0.5)
            return
        except ValueError:
            print("\n올바른 날짜 또는 시간 형식이 아닙니다. 다시 입력해 주세요.\n")
            time.sleep(0.5)

def registered_counsel():
    global n_id
    print("\n---예약된 상담 테이블을 조회합니다.---\n")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM counsel_table WHERE p_id = %s", (user_information[0],))

    table = PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    table.add_rows(rows)

    if (rows):
        print(table)
        time.sleep(1)
        select = input("\n상담 취소를 원하는 테이블의 t_id를 입력해주세요. 상담 취소를 원치 않으시면 'EXIT'를 입력해주세요: ")
        if select.strip():
            if (select.upper() != "EXIT"):
                cursor.execute("SELECT * FROM counsel_table WHERE p_id = %s AND t_id = %s", (user_information[0], select))
                existing_tid = cursor.fetchone()
                if(existing_tid):
                    cursor.execute("UPDATE counsel_table SET status = 'Unoccupied', p_id = NULL WHERE t_id = %s",
                                   (select,))
                    con.commit()
                    print("\n---상담이 취소되었습니다.---\n")
                    con.cursor()
                    cursor.execute("SELECT date FROM counsel_table WHERE t_id = %s", (select,))
                    date = cursor.fetchone()
                    cursor.execute("SELECT s_time FROM counsel_table WHERE t_id = %s", (select,))
                    s_time = cursor.fetchone()
                    cursor.execute("SELECT e_time FROM counsel_table WHERE t_id = %s", (select,))
                    e_time = cursor.fetchone()
                    cursor.execute("INSERT INTO notification (n_id, p_id, message) VALUES (%s, %s, %s)",
                                   (n_id, user_information[0], f'요청하신 날짜 {date}의 {s_time} ~ {e_time} 시간대의 상담이 취소되었습니다.'))
                    con.commit()
                    n_id += 1
                    time.sleep(0.5)
                else:
                    print("\n올바른 t_id를 입력해 주세요.\n")
                    registered_counsel()
            else:
                print("\n---상담 취소를 진행하지 않습니다.---\n")
                time.sleep(0.5)
                patient_main()
        else:
            print("\n올바른 t_id를 입력해 주세요.")
            registered_counsel()
    else:
        print("\n---예약된 상담 테이블이 없습니다.---\n")
        time.sleep(0.5)
        return

def read_writing():
    print("\n---게시된 기사 목록을 조회합니다.---\n")
    writing_choice()

def writing_choice():
    while True:
        print("기사 검색 조건을 지정합니다. 희망하는 조건이 없다면 공백으로 답변해 주세요.\n")
        try:
            title_condition = input("희망하는 기사 제목(부분 검색): ")
            name_condition = input("기자의 이름(부분 검색): ")
            date_condition = input("게시된 날짜(YYYY-MM-DD 형식): ")

            cursor = con.cursor()

            query = "SELECT * FROM writing WHERE (title LIKE %s) AND (j_name LIKE %s)"
            params = [f"%{title_condition}%", f"%{name_condition}%"]

            if date_condition:
                datetime.strptime(date_condition, '%Y-%m-%d')
                query += " AND (date = %s)"
                params.append(date_condition)

            cursor.execute(query, params)

            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            table.add_rows(rows)

            if (rows):
                print(table)
                time.sleep(1)
            else:
                print("\n---조건에 맞는 기사가 없습니다.---\n")
                time.sleep(1)
            return

        except ValueError:
            print("\n올바른 날짜 형식이 아닙니다. 다시 입력해 주세요.\n")
            time.sleep(0.5)

def request_writing_choice():
    while True:
        choice = input("\n원하는 서비스에 해당하는 숫자를 입력해 주세요.\n1. 기사 요청\n2. 기사 요청 조회 및 취소\n")
        if (choice == "1"):
            select_journalist()
            return
        elif (choice == "2"):
            cancel_request_writing()
            return
        else:
            print("\n올바른 입력이 아닙니다. 숫자 1~2 중 하나를 입력해 주세요.\n")

def select_journalist():
    global r_id
    while True:
        print("\n---기사 요청을 위해 현재 가입되어 있는 기자들의 목록을 출력합니다.---\n")
        cursor = con.cursor()
        cursor.execute("SELECT j_id, name, phonenumber FROM journalist")

        table = PrettyTable()
        table.field_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        table.add_rows(rows)

        print(table)
        time.sleep(0.5)

        select = input("\n기사 요청을 할 기자의 j_id를 입력해 주세요. 요청을 원치 않으시면 'EXIT'를 입력해 주세요: ")
        if select.strip():
            if (select.upper() != "EXIT"):
                cursor.execute("SELECT * FROM journalist WHERE j_id = %s", (select,))
                existing_jid = cursor.fetchall()
                if (existing_jid):
                    requested_title = input("\n요청할 기사의 title을 입력해주세요: ")
                    cursor.execute("SELECT * FROM requested_writing WHERE requested_title = %s", (requested_title,))
                    existing_title = cursor.fetchone()
                    if(existing_title):
                        print("\n이미 같은 title을 요청하셨습니다.\n")
                        select_journalist()
                    else:
                        cursor.execute("INSERT INTO requested_writing (r_id, requesting_nickname, requested_title, j_id) VALUES (%s, %s, %s, %s)"
                                           , (r_id, user_information[5], requested_title, select))
                        con.commit()
                        r_id += 1;
                        time.sleep(0.5)
                        print("\n---기사 요청 완료---\n")
                        return
                else:
                    print("\n올바른 j_id를 입력해 주세요.\n")
                    select_journalist()
            else:
                print("\n---기사 요청을 종료합니다.---\n")
                return
        else:
            print("\n올바른 j_id를 입력해 주세요.\n")
            select_journalist()

def cancel_request_writing():
    while True:
        print("\n---기사 요청 목록을 출력합니다.---\n")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM requested_writing WHERE (requesting_nickname = %s)", (user_information[5],))
        existing_nickname = cursor.fetchall()

        if(existing_nickname):
            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
            table.add_rows(existing_nickname)

            print(table)
            time.sleep(0.5)

            select = input("\n취소할 요청의 r_id를 입력해 주세요. 요청을 원치 않으시면 'EXIT'를 입력해 주세요: ")
            if select.strip():
                if (select.upper() != "EXIT"):
                    cursor.execute("SELECT * FROM requested_writing WHERE (requesting_nickname = %s) AND (r_id = %s)", (user_information[5], select))
                    existing_rid = cursor.fetchall()
                    if (existing_rid):
                        cursor.execute(
                            "DELETE FROM requested_writing WHERE r_id = %s", (select,))
                        con.commit()
                        time.sleep(0.5)
                        print("\n---기사 요청 취소를 완료했습니다.---\n")
                    else:
                        print("\n올바른 r_id를 입력해 주세요.\n")
                        cancel_request_writing()
                else:
                    print("\n---기사 요청 취소를 종료합니다.---\n")
                    return
            else:
                print("\n올바른 r_id를 입력해 주세요.\n")
                cancel_request_writing()
        else:
            print("\n---조건에 맞는 기사가 없습니다.---\n")
            time.sleep(1)
            return

def read_notification():
    while True:
        print("\n---현재 알림 목록을 출력합니다.---\n")
        cursor = con.cursor()
        cursor.execute("SELECT n_id, message, created_at FROM notification WHERE p_id = %s ORDER BY created_at DESC",
                       (user_information[0],))
        existing_nid = cursor.fetchall()

        if (existing_nid):
            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
            table.add_rows(existing_nid)

            print(table)
            time.sleep(0.5)

            select = input("\n삭제(읽음 처리)할 알림이 있다면 해당 알림의 n_id를 입력해 주세요. 삭제를 진행하지 않으려면 'EXIT'를 입력해 주세요: ")
            if select.strip():
                if (select.upper() != "EXIT"):
                    cursor.execute("SELECT * FROM notification WHERE (p_id = %s) AND (n_id = %s)",
                                   (user_information[0], select))
                    existing_nid = cursor.fetchall()
                    if (existing_nid):
                        cursor.execute("DELETE FROM notification WHERE (p_id = %s) AND (n_id = %s)",
                                   (user_information[0], select))
                        con.commit()
                        time.sleep(0.5)
                        print("\n---알림 삭제 완료---\n")
                        read_notification()
                        return
                    else:
                        print("\n올바른 n_id를 입력해 주세요.\n")
                        read_notification()
                else:
                    print("\n---알림 열람을 종료합니다.---\n")
                    return
            else:
                print("\n올바른 n_id를 입력해 주세요.\n")
                read_notification()
        else:
            print("\n---현재 알림이 없습니다.---\n")
            return

def patient_logout():
    print("\n로그아웃을 하려면 'OUT'을 입력해 주세요. 종료를 원치 않는다면 다른 문자를 아무거나 입력해 주세요: ")
    islogout = input()
    if islogout.upper() == "OUT":
        print("\n---로그아웃을 진행합니다.---\n")
        initial_choice()
        return
    else:
        print("\n---로그아웃을 진행하지 않습니다.---\n")
        time.sleep(0.5)
        patient_main()
        return

def patient_modify():
    global user_information
    global disease_information
    global medicine_information
    global d_id
    global m_id
    while True:
        print("\n---개인 정보 수정을 위해 개인 정보를 출력합니다.---\n")
        print('1. p_ID: %s' % (user_information[0]))
        print('2. ID: %s' % (user_information[1]))
        print('3. password: %s' % (user_information[2]))
        print('4. name, phonenumber: %s, %s' % (user_information[3], user_information[4]))
        print('5. nickname: %s' % (user_information[5]))
        print("6. diseases:")
        for disease_name in disease_information:
            print('%s' % (disease_name))
        print("7. medicines:")
        for medicine_name in medicine_information:
            print('%s' % (medicine_name))
        select = input("\n위에서 수정을 희망하는 개인 정보의 번호를 선택해 주세요.(3~7번만 변경 가능) 개인 정보 수정을 종료하려면 'EXIT'을 입력해 주세요: ")
        if(select == "3"):
            print("\n---비밀번호를 변경합니다.---\n")
            modified_pw = PW_input()
            cursor = con.cursor()
            cursor.execute("UPDATE patient SET password = %s WHERE p_id = %s",
                        (modified_pw, user_information[0]))
            cursor.execute("SELECT * FROM patient WHERE p_id = %s", (user_information[0],))
            user_information = cursor.fetchone()
            con.commit()
            print("\n---비밀번호 변경 완료---\n")
        elif(select == "4"):
            print("\n---이름과 전화번호를 변경합니다.---\n")
            modified_name, modified_phonenumber = NP_input()
            cursor = con.cursor()
            cursor.execute("UPDATE patient SET name = %s, phonenumber = %s WHERE p_id = %s",
                           (modified_name, modified_phonenumber, user_information[0]))
            cursor.execute("SELECT * FROM patient WHERE p_id = %s", (user_information[0],))
            user_information = cursor.fetchone()
            con.commit()
            print("\n---이름, 전화번호 변경 완료---\n")
        elif(select == "5"):
            print("\n---닉네임을 변경합니다.---\n")
            modified_nname = NNAME_input()
            cursor = con.cursor()
            cursor.execute("UPDATE patient SET nickname = %s WHERE p_id = %s",
                           (modified_nname, user_information[0]))
            cursor.execute("SELECT * FROM patient WHERE p_id = %s", (user_information[0],))
            user_information = cursor.fetchone()
            con.commit()
            print("\n---닉네임 변경 완료---\n")
        elif(select == "6"):
            print("\n---앓고 있는 질환을 변경합니다.---\n")
            modified_disease_list = DISEASE_input()
            cursor = con.cursor()
            cursor.execute("DELETE FROM disease WHERE p_id = %s",
                           (user_information[0],))
            for disease_name in modified_disease_list:
                cursor.execute("INSERT INTO disease (d_id, p_id, disease_name) VALUES (%s, %s, %s)",
                           (d_id, user_information[0], disease_name))
                d_id += 1
            cursor.execute("SELECT disease_name FROM disease WHERE p_id = %s", (user_information[0],))
            disease_information = cursor.fetchall()
            con.commit()
            print("\n---질환 정보 변경 완료---\n")
        elif(select == "7"):
            print("\n---복용 중인 약을 변경합니다.---\n")
            modified_medicine_list = MEDICINE_input()
            cursor = con.cursor()
            cursor.execute("DELETE FROM medicine WHERE p_id = %s",
                           (user_information[0],))
            for medicine_name in modified_medicine_list:
                cursor.execute("INSERT INTO medicine (m_id, p_id, medicine_name) VALUES (%s, %s, %s)",
                               (m_id, user_information[0], medicine_name))
                m_id += 1
            cursor.execute("SELECT medicine_name FROM medicine WHERE p_id = %s", (user_information[0],))
            medicine_information = cursor.fetchall()
            con.commit()
            print("\n---복용 약 정보 변경 완료---\n")
        elif (select.upper() == "EXIT"):
            print("---개인 정보 수정을 종료합니다.---")
            patient_main()
            return
        else:
            print("\n올바른 입력이 아닙니다. 숫자 3~7 중 하나, 또는 'EXIT'을 입력해 주세요.\n")
def patient_sign_out():
    print("\n---회원 탈퇴를 선택하셨습니다.---\n")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM counsel_table, requested_writing WHERE (p_id = %s) OR (requesting_nickname = %s)",
                   (user_information[0], user_information[5]))
    existing_table = cursor.fetchone()
    if (existing_table):
        print("현재 현재 상담 예약이나 기사 요청이 되어 있는 상태입니다. 회원 탈퇴 시 해당 정보가 모두 사라집니다.\n")
    select = input("회원 탈퇴를 희망하시면 'DELETE'를 입력해 주세요. 회원 탈퇴를 희망하지 않는다면 다른 문자를 아무거나 입력해 주세요: ")
    if(select.upper() == "DELETE"):
        print("\n---회원 탈퇴를 진행합니다.---\n")
        cursor = con.cursor()
        if (existing_table):
            cursor.execute("UPDATE counsel_table SET status = 'Unoccupied', p_id = NULL WHERE p_id = %s",(user_information[0],))
            cursor.execute("DELETE FROM requested_writing WHERE requesting_nickname = %s", (user_information[5],))
        cursor.execute("DELETE FROM notification WHERE p_id = %s", (user_information[0],))
        cursor.execute("DELETE FROM disease WHERE p_id = %s", (user_information[0],))
        cursor.execute("DELETE FROM medicine WHERE p_id = %s", (user_information[0],))
        cursor.execute("DELETE FROM patient WHERE p_id = %s", (user_information[0],))
        con.commit()
        time.sleep(1)
        print("\n---회원 탈퇴가 완료되었습니다. 감사합니다.---\n")
        initial_choice()
        return
    else:
        ("\n---회원 탈퇴를 진행하지 않습니다.---\n")
        patient_main()
        return
def counselor_main():
    while True:
        choice = input("\n원하는 서비스에 해당하는 숫자를 입력해 주세요.\n1. 상담 테이블 작성 / 조회 및 삭제\n2. 환자 정보 조회\n"
                       "3. 로그아웃\n4. 개인 정보 조회 및 수정\n5. 회원 탈퇴\n")
        if (choice == "1"):
            counselor_counsel_choice()
        elif (choice == "2"):
            read_patient_inform()
        elif (choice == "3"):
            counselor_logout()
        elif (choice == "4"):
            counselor_modify()
        elif (choice == "5"):
            counselor_sign_out()
        else:
            print("\n올바른 입력이 아닙니다. 숫자 1~5 중 하나를 입력해 주세요.\n")

def counselor_counsel_choice():
    while True:
        choice = input("\n원하는 서비스에 해당하는 숫자를 입력해 주세요.\n1. 건강 상담 일정 작성\n2. 건강 상담 일정 조회 및 삭제\n3. 뒤로가기\n")
        if(choice == "1"):
            writing_counsel()
            return
        elif(choice == "2"):
            read_delete_counsel()
            return
        elif (choice == "3"):
            counselor_main()
            return
        else:
            print("\n올바른 입력이 아닙니다. 숫자 1~3 중 하나를 입력해 주세요.\n")
def writing_counsel():
    global t_id
    while True:
        print("\n---건강 상담 일정을 작성합니다. 작성을 중지하려면 EXIT을 입력해 주세요.---\n")
        try:
            date_input = input("상담 날짜(YYYY-MM-DD 형식): ")
            if(date_input.upper() == "EXIT"):
                print("\n---상담 일정 작성을 중지합니다.---\n")
                counselor_main()
                break
            stime_input = input("상담 시작 시간 (HH:MM 형식): ")
            if (stime_input.upper() == "EXIT"):
                print("\n---상담 일정 작성을 중지합니다.---\n")
                counselor_main()
                break
            etime_input = input("상담 종료 시간 (HH:MM 형식): ")
            if (etime_input.upper() == "EXIT"):
                print("\n---상담 일정 작성을 중지합니다.---\n")
                counselor_main()
                break

            stime_input += ":00" if stime_input else ""
            etime_input += ":00" if etime_input else ""

            datetime.strptime(date_input, '%Y-%m-%d')
            datetime.strptime(stime_input, '%H:%M:%S')
            datetime.strptime(etime_input, '%H:%M:%S')

            cursor = con.cursor()
            cursor.execute("INSERT INTO counsel_table (t_id, c_name, c_phonenumber, date, s_time, e_time, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (t_id, user_information[3], user_information[4], date_input, stime_input, etime_input, 'Unoccupied'))
            t_id += 1
            con.commit()

            print("\n---건강 상담 일정 작성이 완료되었습니다.---\n")
            time.sleep(0.5)

        except ValueError:
            print("\n올바른 날짜 또는 시간 형식이 아닙니다. 다시 입력해 주세요.\n")
            time.sleep(0.5)
def read_delete_counsel():
    while True:
        print("\n---작성하신 건강 상담 일정 목록을 출력합니다.---\n")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM counsel_table WHERE (c_name = %s) AND (c_phonenumber = %s)", (user_information[3], user_information[4]))
        existing_table = cursor.fetchall()

        if (existing_table):
            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
            table.add_rows(existing_table)

            print(table)
            time.sleep(0.5)

            select = input("\n취소할 건강 상담 일정의 t_id를 입력해 주세요. 상담 일정 취소를 원치 않으시면 'EXIT'를 입력해 주세요: ")
            if select.strip():
                if (select.upper() != "EXIT"):
                    cursor.execute("SELECT * FROM counsel_table WHERE (c_name = %s) AND (c_phonenumber = %s) AND (t_id = %s)",
                                   (user_information[3], user_information[4], select))
                    existing_tid = cursor.fetchall()
                    if (existing_tid):
                        cursor.execute(
                            "DELETE FROM counsel_table WHERE t_id = %s", (select,))
                        con.commit()
                        time.sleep(0.5)
                        print("\n---건강 상담 일정 취소를 완료했습니다.---\n")
                    else:
                        print("\n올바른 t_id를 입력해 주세요.\n")
                        read_delete_counsel()
                else:
                    print("\n---건강 상담 일정 취소를 종료합니다.---\n")
                    counselor_main()
                    return
            else:
                print("\n올바른 t_id를 입력해 주세요.\n")
                read_delete_counsel()
        else:
            print("\n---작성하신 건강 상담 일정이 없습니다.---\n")
            time.sleep(1)
            return
def read_patient_inform():
    print("\n---예약되어 있는 건강 상담 목록을 조회합니다. 희망하는 조건이 없다면 공백으로 답변해 주세요.---\n")
    while True:
        try:
            date_condition = input("상담 날짜(YYYY-MM-DD 형식): ")
            stime_condition = input("상담 시작 시간 (HH:MM 형식): ")
            etime_condition = input("상담 종료 시간 (HH:MM 형식): ")

            stime_condition += ":00" if stime_condition else ""
            etime_condition += ":00" if etime_condition else ""

            cursor = con.cursor()

            query = "SELECT * FROM counsel_table WHERE (c_name = %s) AND (c_phonenumber = %s) AND (status = 'Occupied')"
            params = [user_information[3], user_information[4]]

            if date_condition:
                datetime.strptime(date_condition, '%Y-%m-%d')
                query += " AND (date = %s)"
                params.append(date_condition)
            if stime_condition:
                datetime.strptime(stime_condition, '%H:%M:%S')
                query += " AND (s_time >= %s)"
                params.append(stime_condition)
            if etime_condition:
                datetime.strptime(etime_condition, '%H:%M:%S')
                query += " AND (e_time <= %s)"
                params.append(etime_condition)

            cursor.execute(query, params)

            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            table.add_rows(rows)

            if (rows):
                print(table)
                select = input("\n환자 정보를 열람하고자 하는 일정의 t_id를 입력해주세요. 환자 정보 열람을 원치 않으시면 'EXIT'를 입력해주세요: ")
                if select.strip():
                    if (select.upper() != "EXIT"):
                        cursor.execute("SELECT p_id FROM counsel_table WHERE (t_id = %s) AND (c_name = %s) AND (c_phonenumber = %s) AND (status = 'Occupied')",
                                       (select, user_information[3], user_information[4]))
                        pid = cursor.fetchone()
                        if (pid):
                            print("\n---환자의 정보를 출력합니다.---\n")
                            cursor.execute("SELECT * FROM patient WHERE p_id = %s", (pid,))
                            p_inform = cursor.fetchone()
                            cursor.execute("SELECT disease_name FROM disease WHERE p_id = %s", (pid,))
                            p_dis = cursor.fetchall()
                            cursor.execute("SELECT medicine_name FROM medicine WHERE p_id = %s", (pid,))
                            p_med = cursor.fetchall()
                            print('1. name, phonenumber: %s, %s' % (p_inform[3], p_inform[4]))
                            print("2. diseases:")
                            for disease_name in p_dis:
                                print('%s' % (disease_name))
                            print("3. medicines:")
                            for medicine_name in p_med:
                                print('%s' % (medicine_name))
                            time.sleep(0.5)
                            print("\n---환자 정보 출력을 완료했습니다.---\n")
                        else:
                            print("\n올바른 t_id를 입력해 주세요.\n")
                            read_patient_inform()
                    else:
                        print("\n---환자 정보 열람을 진행하지 않습니다.---\n")
                        time.sleep(0.5)
                        counselor_main()
                else:
                    print("\n올바른 t_id를 입력해 주세요.\n")
                    read_patient_inform()
            else:
                print("\n---예약된 상담 일정이 없습니다.---\n")
                time.sleep(0.5)
            return
        except ValueError:
            print("\n올바른 날짜 또는 시간 형식이 아닙니다. 다시 입력해 주세요.\n")
            time.sleep(0.5)
def counselor_logout():
    print("\n로그아웃을 하려면 'OUT'을 입력해 주세요. 종료를 원치 않는다면 다른 문자를 아무거나 입력해 주세요: ")
    islogout = input()
    if islogout.upper() == "OUT":
        print("\n---로그아웃을 진행합니다.---\n")
        initial_choice()
        return
    else:
        print("\n---로그아웃을 진행하지 않습니다.---\n")
        time.sleep(0.5)
        counselor_main()
        return
def counselor_modify():
    global user_information
    while True:
        print("\n---개인 정보 수정을 위해 개인 정보를 출력합니다.---\n")
        print('1. c_ID: %s' % (user_information[0]))
        print('2. ID: %s' % (user_information[1]))
        print('3. password: %s' % (user_information[2]))
        print('4. name, phonenumber: %s, %s' % (user_information[3], user_information[4]))
        select = input("\n위에서 수정을 희망하는 개인 정보의 번호를 선택해 주세요.(3~4번만 변경 가능) 개인 정보 수정을 종료하려면 'EXIT'을 입력해 주세요: ")
        if (select == "3"):
            print("\n---비밀번호를 변경합니다.---\n")
            modified_pw = PW_input()
            cursor = con.cursor()
            cursor.execute("UPDATE counselor SET password = %s WHERE c_id = %s",
                           (modified_pw, user_information[0]))
            cursor.execute("SELECT * FROM counselor WHERE c_id = %s", (user_information[0],))
            user_information = cursor.fetchone()
            con.commit()
            print("\n---비밀번호 변경 완료---\n")
        elif (select == "4"):
            print("\n---이름과 전화번호를 변경합니다.---\n")
            modified_name, modified_phonenumber = NP_input()
            cursor = con.cursor()
            cursor.execute("UPDATE counselor SET name = %s, phonenumber = %s WHERE c_id = %s",
                           (modified_name, modified_phonenumber, user_information[0]))
            cursor.execute("SELECT * FROM counselor WHERE c_id = %s", (user_information[0],))
            user_information = cursor.fetchone()
            con.commit()
            print("\n---이름, 전화번호 변경 완료---\n")
        elif (select.upper() == "EXIT"):
            print("---개인 정보 수정을 종료합니다.---")
            counselor_main()
            return
        else:
            print("\n올바른 입력이 아닙니다. 숫자 3~4 중 하나, 또는 'EXIT'을 입력해 주세요.\n")
def counselor_sign_out():
    print("\n---회원 탈퇴를 선택하셨습니다.---\n")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM counsel_table WHERE c_id = %s",
                   (user_information[0],))
    existing_table = cursor.fetchone()
    if (existing_table):
        print("현재 현재 상담 예약을 작성한 상태입니다. 회원 탈퇴 시 해당 정보가 모두 사라집니다.\n")
    select = input("회원 탈퇴를 희망하시면 'DELETE'를 입력해 주세요. 회원 탈퇴를 희망하지 않는다면 다른 문자를 아무거나 입력해 주세요: ")
    if (select.upper() == "DELETE"):
        print("\n---회원 탈퇴를 진행합니다.---\n")
        cursor = con.cursor()
        if (existing_table):
            cursor.execute("DELETE FROM counsel_table WHERE c_id = %s", (user_information[0],))
        cursor.execute("DELETE FROM counselor WHERE c_id = %s", (user_information[0],))
        con.commit()
        time.sleep(1)
        print("\n---회원 탈퇴가 완료되었습니다. 감사합니다.---\n")
        initial_choice()
        return
    else:
        ("\n---회원 탈퇴를 진행하지 않습니다.---\n")
        counselor_main()
        return
def journalist_main():
    while True:
        choice = input("\n원하는 서비스에 해당하는 숫자를 입력해 주세요.\n1. 기사 링크 작성 / 작성한 기사 링크 조회 및 삭제\n2. 기사 요청 확인\n"
                       "3. 로그아웃\n4. 개인 정보 조회 및 수정\n5. 회원 탈퇴\n")
        if (choice == "1"):
            journal_choice()
        elif (choice == "2"):
            read_request()
        elif (choice == "3"):
            journalist_logout()
        elif (choice == "4"):
            journalist_modify()
        elif (choice == "5"):
            journalist_sign_out()
        else:
            print("\n올바른 입력이 아닙니다. 숫자 1~5 중 하나를 입력해 주세요.\n")

def journal_choice():
    while True:
        choice = input("\n원하는 서비스에 해당하는 숫자를 입력해 주세요.\n1. 기사 링크 작성\n2. 작성한 기사 조회 및 삭제\n3. 뒤로가기\n")
        if (choice == "1"):
            writing_journal()
            return
        elif (choice == "2"):
            read_delete_journal()
            return
        elif (choice == "3"):
            journalist_main()
            return
        else:
            print("\n올바른 입력이 아닙니다. 숫자 1~3 중 하나를 입력해 주세요.\n")

def writing_journal():
    global w_id
    global n_id
    while True:
        print("\n---기사 링크를 작성합니다. 작성을 중지하려면 EXIT을 입력해 주세요.---\n")
        try:
            title_input = input("title: ")
            if(title_input.upper() == "EXIT"):
                print("\n---기사 링크 작성을 중지합니다.---\n")
                journalist_main()
                break
            date_input = input("기사 작성 날짜(YYYY-MM-DD 형식): ")
            if (date_input.upper() == "EXIT"):
                print("\n---기사 링크 작성을 중지합니다.---\n")
                journalist_main()
                break
            link_input = input("링크 ('https://'로 시작해야 함): ")
            if (link_input.upper() == "EXIT"):
                print("\n---기사 링크 작성을 중지합니다.---\n")
                journalist_main()
                break

            if not link_input.startswith('https://'):
                print("\n링크는 'https://'로 시작해야 합니다. 다시 입력해 주세요.\n")
                time.sleep(0.5)
                continue

            datetime.strptime(date_input, '%Y-%m-%d')

            cursor = con.cursor()
            cursor.execute("INSERT INTO writing (w_id, title, j_name, j_phonenumber, date, link) VALUES (%s, %s, %s, %s, %s, %s)",
            (w_id, title_input, user_information[3], user_information[4], date_input, link_input))
            w_id += 1
            con.commit()

            print("\n---기사 링크 작성이 완료되었습니다.---\n")
            time.sleep(0.5)

            cursor = con.cursor()
            cursor.execute("SELECT requesting_nickname FROM writing w, requested_writing r WHERE (w.title = r.requested_title) AND (w.w_id = %s)",
                                           (w_id - 1,))
            nickname = cursor.fetchone()
            if(nickname):
                cursor.execute("SELECT p_id FROM patient WHERE nickname = %s", (nickname))
                pid = cursor.fetchone()
                cursor.execute("INSERT INTO notification (n_id, p_id, message) VALUES (%s, %s, %s)",
                               (n_id, pid, f'요청하신 {title_input} 제목의 기사가 작성되었습니다.'))
                print("---요청과 같은 제목의 기사를 작성하셨습니다. 해당 기사를 요청한 환자에게 알림을 보냅니다.---\n")
                n_id += 1

        except ValueError:
            print("\n올바른 날짜 형식이 아닙니다. 다시 입력해 주세요.\n")
            time.sleep(0.5)
    return
def read_delete_journal():
    while True:
        print("\n---작성하신 기사 링크 목록을 출력합니다.---\n")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM writing WHERE (j_name = %s) AND (j_phonenumber = %s)", (user_information[3], user_information[4]))
        existing_table = cursor.fetchall()

        if (existing_table):
            table = PrettyTable()
            table.field_names = [desc[0] for desc in cursor.description]
            table.add_rows(existing_table)

            print(table)
            time.sleep(0.5)

            select = input("\n삭제할 기사 링크의 w_id를 입력해 주세요. 삭제를 원치 않으시면 'EXIT'를 입력해 주세요: ")
            if select.strip():
                if (select.upper() != "EXIT"):
                    cursor.execute("SELECT * FROM writing WHERE (j_name = %s) AND (j_phonenumber = %s) AND (w_id = %s)",
                                   (user_information[3], user_information[4], select))
                    existing_tid = cursor.fetchall()
                    if (existing_tid):
                        cursor.execute(
                            "DELETE FROM writing WHERE w_id = %s", (select,))
                        con.commit()
                        time.sleep(0.5)
                        print("\n---기사 링크 삭제를 완료했습니다.---\n")
                    else:
                        print("\n올바른 w_id를 입력해 주세요.\n")
                        read_delete_journal()
                else:
                    print("\n---기사 링크 삭제를 종료합니다.---\n")
                    journalist_main()
                    return
            else:
                print("\n올바른 w_id를 입력해 주세요.\n")
                read_delete_journal()
        else:
            print("\n---작성하신 기사 링크가 없습니다.---\n")
            time.sleep(1)
            return
def read_request():
    print("\n---기사 요청 목록을 조회합니다.\n")
    while True:
        cursor = con.cursor()

        query = "SELECT * FROM requested_writing WHERE (j_id = %s) AND (status = 'Occupied')"
        params = [user_information[0],]

        cursor.execute("SELECT requesting_nickname, requested_title, created_at FROM requested_writing ORDER BY created_at DESC")

        table = PrettyTable()
        table.field_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        table.add_rows(rows)

        if (rows):
            print("\n---기사 요청 목록을 출력합니다.---\n")
            print(table)
            print("\n---기사 요청 목록 출력을 완료했습니다.---\n")
        else:
            print("\n---기사 요청 목록이 없습니다.---\n")
            time.sleep(0.5)
        return
def journalist_logout():
    print("\n로그아웃을 하려면 'OUT'을 입력해 주세요. 종료를 원치 않는다면 다른 문자를 아무거나 입력해 주세요: ")
    islogout = input()
    if islogout.upper() == "OUT":
        print("\n---로그아웃을 진행합니다.---\n")
        initial_choice()
        return
    else:
        print("\n---로그아웃을 진행하지 않습니다.---\n")
        time.sleep(0.5)
        journalist_main()
        return
def journalist_modify():
    global user_information
    while True:
        print("\n---개인 정보 수정을 위해 개인 정보를 출력합니다.---\n")
        print('1. j_ID: %s' % (user_information[0]))
        print('2. ID: %s' % (user_information[1]))
        print('3. password: %s' % (user_information[2]))
        print('4. name, phonenumber: %s, %s' % (user_information[3], user_information[4]))
        select = input("\n위에서 수정을 희망하는 개인 정보의 번호를 선택해 주세요.(3~4번만 변경 가능) 개인 정보 수정을 종료하려면 'EXIT'을 입력해 주세요: ")
        if (select == "3"):
            print("\n---비밀번호를 변경합니다.---\n")
            modified_pw = PW_input()
            cursor = con.cursor()
            cursor.execute("UPDATE journalist SET password = %s WHERE j_id = %s",
                           (modified_pw, user_information[0]))
            cursor.execute("SELECT * FROM journalist WHERE j_id = %s", (user_information[0],))
            user_information = cursor.fetchone()
            con.commit()
            print("\n---비밀번호 변경 완료---\n")
        elif (select == "4"):
            print("\n---이름과 전화번호를 변경합니다.---\n")
            modified_name, modified_phonenumber = NP_input()
            cursor = con.cursor()
            cursor.execute("UPDATE journalist SET name = %s, phonenumber = %s WHERE j_id = %s",
                           (modified_name, modified_phonenumber, user_information[0]))
            cursor.execute("SELECT * FROM journalist WHERE j_id = %s", (user_information[0],))
            user_information = cursor.fetchone()
            con.commit()
            print("\n---이름, 전화번호 변경 완료---\n")
        elif (select.upper() == "EXIT"):
            print("---개인 정보 수정을 종료합니다.---")
            counselor_main()
            return
        else:
            print("\n올바른 입력이 아닙니다. 숫자 3~4 중 하나, 또는 'EXIT'을 입력해 주세요.\n")
def journalist_sign_out():
    print("\n---회원 탈퇴를 선택하셨습니다.---\n")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM writing w, requested_writing r WHERE ((w.j_name = %s) AND (w.j_phonenumber = %s)) OR (w.j_id = %s)",
                   (user_information[3], user_information[4], user_information[0]))
    existing_table = cursor.fetchone()
    if (existing_table):
        print("현재 작성된 기사나 기사 요청이 존재합니다. 회원 탈퇴 시 해당 정보가 모두 사라집니다.\n")
    select = input("회원 탈퇴를 희망하시면 'DELETE'를 입력해 주세요. 회원 탈퇴를 희망하지 않는다면 다른 문자를 아무거나 입력해 주세요: ")
    if (select.upper() == "DELETE"):
        print("\n---회원 탈퇴를 진행합니다.---\n")
        cursor = con.cursor()
        if (existing_table):
            cursor.execute("DELETE FROM writing WHERE (j_name = %s) AND (j_phonenumber = %s)", (user_information[3], user_information[4]))
            cursor.execute("DELETE FROM requested_writing WHERE j_id = %s", (user_information[0],))
        cursor.execute("DELETE FROM journalist WHERE j_id = %s", (user_information[0],))
        con.commit()
        time.sleep(1)
        print("\n---회원 탈퇴가 완료되었습니다. 감사합니다.---\n")
        initial_choice()
        return
    else:
        ("\n---회원 탈퇴를 진행하지 않습니다.---\n")
        counselor_main()
        return


initial()