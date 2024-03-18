# Database Project

3학년 2학기 데이터베이스 수업 중 진행한 프로젝트입니다.

------------

## 사용한 언어 및 라이브러리

1. 사용한 언어: python
2. 사용한 라이브러리:  
import psycopg2  
import sys  
import time  
from datetime import datetime  
from prettytable import PrettyTable  

------------

## 프로그램 실행
  
Release v1.0.0 내의 "DBProject_201624587.exe" 파일 실행  

## 프로그램 코드 확인
  
Repository 내의 "DBProject_201624587.py" 파일에서 확인  

## 프로그램 매뉴얼
  
Repository 내의 "project program manual_201624587.docx" 파일에서 확인

------------

## 프로젝트 개요

### 프로젝트 주제

‘만관부’ 어플리케이션은 만성질환자 관리를 부탁하는 어플리케이션으로, 만성질환 관리를 도와주는 기능을 한다.

### 프로젝트 목표

만성질환은 쉽게 낫지 않고 잘 관리하지 않으면 빠르게 악화될 수 있기 때문에, 장기적으로 꾸준한 관리가 필요하다.  
이 프로젝트는 이런 만성질환자들에게 정보 전달을 목적으로 한 가상의 어플리케이션을 가정하고, 내부 시스템을 구현한다.  
  
해당 어플리케이션의 목표는 크게 두 가지로 나눌 수 있다.  
첫 번째는, 환자와 건강 상담사와의 상담 신청을 매개해 주는 것이다. 건강 상담사는 환자가 앓고 있는 질환과 복용 중인 약을 열람할 수 있다.  
두 번째는, 만성질환자들에게 연구 결과, 전문가 인터뷰 등이 담긴 기사를 제공해 주는 것이다.  

### 프로젝트의 차별성, 장점

1. 사용자의 잘못된 입력에 대해 이중 장치가 되어있다.  
데이터베이스 상의 타입 제한을 두었고, 이용자가 해당 제한을 벗어나는 입력을 한다면 프로그램이 강제적으로 종료될 수 있다.  
이런 현상을 방지하기 위해 에러 메시지를 출력하고, 다시 입력할 수 있도록 되돌리는 동작들을 세부적으로 구현했다.  
또한, 회원 탈퇴 시 foreign key가 참조하고 있는 데이터가 삭제되었을 때의 foreign key constraint 에러를 방지하기 위해, 별도의 동작을 구현했다.  
예를 들면, 기자가 작성한 글이 게시된 상태에서 회원 탈퇴를 하면, 작성한 글을 먼저 삭제한 후, 기자의 정보를 삭제하도록 했다.  

2. 각 이용자에 대한 다양한 기능이 구현되어 있다.  
현재 로그인 되어있는 이용자의 정보를 저장함으로써, cursor.execute를 통한 SQL 쿼리 내의 변수 처리를 효율적으로 구현했다.  
이런 방식으로 다양한 조건을 통한 상담 테이블 검색, 회원 정보 수정, 알림 전송 등의 다양한 기능을 구현했다.  

------------

## 사용자(Users) / 역할(Roles)

만성질환자 관리 시스템을 이용하는 사용자에는 만성질환자(Patient), 건강 상담사(Counselor), 기자(Journalist)가 있다.  

만성질환자는 건강 상담 예약 테이블을 조회하여 건강 상담을 예약, 취소하거나, 기자가 게시한 기사를 열람하거나, 기자에게 기사를 요청할 수 있다.  

건강 상담사는 건강 상담 예약 테이블을 작성하여 환자들에게 건강 상담을 제공하고, 상담을 요청한 환자의 데이터를 열람할 수 있다.  

기자는 외부 링크에서 기사를 작성하여 자신의 기사에 대한 링크를 업로드 할 수 있다.  
본인이 작성한 글에 대해 링크를 삭제할 수도 있고, 환자가 요청한 기사 주제에 대해 열람할 수 있다.  

------------

## 기능(Functions)

### 1. 만성질환자(Patient)
  1) 회원 가입  
    - 앓고 있는 질환, 복용 중인 약 정보 등을 포함하여 정보를 입력함으로써 회원가입한다.  
    - 만성질환자 뿐만이 아닌 모든 이용자들에 대해 같은 아이디, (이름, 전화번호)쌍 등이 중복되지 않도록 구현했다.  
    - INSERT INTO ~ VALUES를 이용해 테이블에 새로운 정보를 추가한다.    
  2) 건강 상담 조회 및 신청 / 신청된 상담 조회 및 취소  
    - 예약 가능한 테이블을 조회하고, 예약을 신청할 수 있다.  
    - 또는 자신이 예약한 상담에 대한 테이블을 조회하고, 예약을 취소할 수 있다.  
    - 테이블 조회 시 상담사 이름(부분 검색), 날짜, 시간 등에 대한 조건을 부여할 수 있다.  
    - 예약이 완료/취소되면 환자에게 알림이 간다.  
    - SELECT로 테이블을 조회하고, UPDATE로 예약 신청/취소 여부를 조절한다. 알림 테이블에 INSERT를 하여 환자에게 알림을 전송한다.  
  3) 만성질환 기사 목록 조회  
    - 기자가 작성한 기사 목록을 조회한다.  
    - SELECT로 조회할 수 있다.  
  4) 만성질환 기사 요청 / 조회 및 취소  
    - 기자 목록을 열람하고, 한 명의 기자를 선택하여 기사를 요청한다.  
    - 본인이 요청한 기사 목록을 열람하고, 요청을 취소할 수 있다.  
    - INSERT로 requested_writing 테이블에 요청 사항이 올라간다.  
    - DELETE로 요청을 취소(삭제)한다.  
  5) 알림 목록 열람  
    - 건강 상담 예약/취소, 요청한 기사가 작성되었을 때 알림을 전송받을 수 있다.  
    - ‘읽음’ 처리하지 않은 알림이 존재할 시 메인 화면에서 알림이 있다는 메시지가 출력된다.  
    - SELECT로 알림을 불러온 뒤, DELETE로 ‘읽음’ 처리(삭제)한다.  
  6) 로그아웃  
    - 로그아웃을 하여 초기화면으로 돌아간다.  
  7) 개인정보 수정  
    - 자신의 개인 정보를 열람하고, 수정한다.  
    - 비밀번호가 변경되면 로그아웃 후 재로그인 시 변경된 비밀번호를 입력해야 한다.  
    - UPDATE, INSERT를 통해 정보를 변경한다.  
  8) 회원 탈퇴  
    - 자신의 개인 정보를 모두 삭제한다.  
    - 상담 요청이나 기사 요청이 되어있는 경우, 해당 요청들의 존재를 알린다. 그래도 회원 탈퇴에 동의한다면 예약된 상담들을 ‘Unoccupied’ 상태로 변경하고, 기사 요청들을 삭제한다.  
    - UPDATE, DELETE 등을 통해 정보를 변경, 삭제한다.  
  
### 2. 건강상담사(Counselor)  
  1) 회원 가입  
    - 건강상담사 뿐만이 아닌 모든 이용자들에 대해 같은 아이디, (이름, 전화번호)쌍 등이 중복되지 않도록 구현했다.  
    - INSERT INTO ~ VALUES를 이용해 테이블에 새로운 정보를 추가한다.  
  2) 상담 테이블 작성 / 조회 및 삭제  
    - 날짜, 시간을 입력해 건강 상담 테이블을 작성하거나, 자신이 작성한 테이블을 조회 후 삭제할 수 있다.  
    - INSERT로 작성, SELECT로 조회, DELETE로 삭제한다.  
  3) 환자 정보 조회  
    - 자신이 게시한 상담 테이블에 예약한 환자에 대한 이름, 전화번호, 질환, 복용 약을 조회할 수 있다.  
  4) 로그아웃  
    - 로그아웃을 하여 초기화면으로 돌아간다.  
  5) 개인정보 수정  
    - 자신의 개인 정보를 열람하고, 수정한다.  
    - 비밀번호가 변경되면 로그아웃 후 재로그인 시 변경된 비밀번호를 입력해야 한다.  
    - UPDATE를 통해 정보를 변경한다.  
  6) 회원 탈퇴  
    - 자신의 개인 정보를 모두 삭제한다.  
    - 작성한 상담 테이블이 존재하는 경우, 해당 테이블의 존재를 알린다. 그 래도 회원 탈퇴에 동의한다면 자신의 상담 테이블을 모두 삭제한다.  
    - DELETE를 통해 정보를 삭제한다.  
  
### 3. 기자(Journalist)  
  1) 기사 링크 작성 / 작성한 기사 링크 조회 및 삭제  
    - 자신의 기사에 대한 링크를 올리거나, 자신이 작성한 기사 링크를 조회하고, 삭제할 수 있다.  
    - 환자가 자신에게 요청한 title과 동일한 title의 기사를 작성하면, 해당 환자에게 알림이 전송된다.  
    - INSERT로 작성, SELECT로 조회, DELETE로 삭제한다.  
  2) 기사 요청 확인  
    - 환자가 자신에게 요청한 기사를 확인한다.  
    - SELECT로 조회한다.  
  3) 로그아웃  
    - 로그아웃을 하여 초기화면으로 돌아간다.  
  4) 개인정보 수정  
    - 자신의 개인 정보를 열람하고, 수정한다.  
    - 비밀번호가 변경되면 로그아웃 후 재로그인 시 변경된 비밀번호를 입력해야 한다.  
    - UPDATE를 통해 정보를 변경한다.  
  5) 회원 탈퇴  
    - 자신의 개인 정보를 모두 삭제한다.  
    - 작성한 기사나 기사 요청이 존재하는 경우, 해당 테이블의 존재를 알린다. 그래도 회원 탈퇴에 동의한다면 해당 테이블을 모두 삭제한다.  
    - DELETE를 통해 정보를 삭제한다.  
  
------------

## 데이터베이스 스키마 및 다이어그램

### 1. Patient 관련 스키마  
```
patient (  
    p_id INT PRIMARY KEY,  
    id VARCHAR(12) UNIQUE,  
    password VARCHAR(16),  
    name VARCHAR(20),  
    phonenumber VARCHAR(12),  
    nickname VARCHAR(12) UNIQUE,  
    CONSTRAINT unique_n_p_pair UNIQUE (name, phonenumber)  
)  
disease (  
    d_id INT PRIMARY KEY,  
    p_id INT,  
    disease_name VARCHAR(30),  
    FOREIGN KEY (p_id) REFERENCES patient(p_id)  
)  
medicine (  
    m_id INT PRIMARY KEY,  
    p_id INT,  
    medicine_name VARCHAR(30),  
    FOREIGN KEY (p_id) REFERENCES patient(p_id)  
)  
notification (  
    n_id INT PRIMARY KEY,  
    p_id INT,  
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    message VARCHAR(255),  
    FOREIGN KEY (p_id) REFERENCES patient(p_id)  
)
```
  
### 2. Counselor 관련 스키마  
```
counselor (  
    c_id INT PRIMARY KEY,  
    id VARCHAR(12) UNIQUE,  
    password VARCHAR(16),  
    name VARCHAR(20),  
    phonenumber VARCHAR(12),  
    CONSTRAINT unique_n_p_pair UNIQUE (name, phonenumber)  
)  
counsel_table (  
    t_id INT PRIMARY KEY,  
    c_name VARCHAR(20),  
    c_phonenumber VARCHAR(12),  
    date DATE,  
    s_time TIME,  
    e_time TIME,  
    status VARCHAR(10), // ‘Occupied’ 또는 ‘Unoccupied’  
    p_id INT,  
    FOREIGN KEY (c_name, c_phonenumber) REFERENCES counselor(name, phonenumber),  
    FOREIGN KEY (p_ID) REFERENCES patient(p_ID)  
)
``` 
  
### 3. Journalist 관련 스키마  
```
journalist (  
    j_id INT PRIMARY KEY,  
    id VARCHAR(12) UNIQUE,  
    password VARCHAR(16),  
    name VARCHAR(20),  
    phonenumber VARCHAR(12),  
    CONSTRAINT unique_n_p_pair UNIQUE (name, phonenumber)  
)  
writing (  
    w_id INT PRIMARY KEY,  
    title VARCHAR(50),  
    j_name VARCHAR(20),  
    j_phonenumber VARCHAR(12),  
    date DATE,  
    link VARCHAR(255) CHECK (link LIKE 'https://%'),  
    FOREIGN KEY (j_name, j_phonenumber) REFERENCES journalist(name, phonenumber)  
)  
requested_writing (  
    r_id INT PRIMARY KEY,  
    requesting_nickname VARCHAR(12),  
    requested_title VARCHAR(255),  
    j_id INT,  
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    FOREIGN KEY (requesting_nickname) REFERENCES patient(nickname),  
    FOREIGN KEY (j_id) REFERENCES journalist(j_id)  
)
```
