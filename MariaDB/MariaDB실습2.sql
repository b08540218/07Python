/*
테이블 생성하기제약조건
	PRIMARY KEY : 기본키 지정. 
*/

#1. 숫자형으로 구성된 테이블
CREATE TABLE tb_int (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	num1 TINYINT UNSIGNED NOT NULL,
	num2 SMALLINT NOT NULL,
	num3 MEDIUMINT DEFAULT '100',
	num4 BIGINT ,
	
	fnum1 FLOAT(10, 5) NOT NULL,
	fnum2 DOUBLE(20,10)
);
DESC tb_int;

/*
레코드 입력하기
형식1 : 일련번호 idx 컬럼은 insert문애서 생략하고 작성한다.
	자동증가 컬럼으로 지정되었으므로 순차적인 번호가 자동으로
	부여된다. 즉, 자동증가 컬럼은 insert문에서 생략하는게 기본이다.
*/
INSERT INTO tb_int (num1,num2,num3,num4,num4,fnum1,fnum2)
VALUE (123, 12345, 1234567, 1234567890,
			12345.12345, 1234567890.1234567890);
SELECT * FROM tb_int;
			
/*
형식2 : inset문 작성시 컬럼을 명시하지 않으면 전체 컬럼에 대해
	입력값을 기술해야 하므로 실행시 오류가 발생할 수 있어 권장하지
	않는다.
*/
INSERT INTO tb_int
VALUE (2, 123, 12345, 1234567, 1234567890,
			12345.12345, 1234567890.1234567890);
			
/*
CURRENT_TIMESTAMP : 날짜형식으로 지정된 컬럼에 디폴트값으로 현재시간을
	입력할때 사용한다.
NOW() : 날짜 형식으로 지정된 컬럼에 현재시간을 입력한다. 초단위까지의
시간이 입력된다. 오라클의 sysdate와 동일한 역할을 한다.
*/
CREATE TABLE tb_date(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	DATE1 DATE NOT NULL,
	DATE2 DATETIME DEFAULT current_timestamp
);
DESC tb_date;


INSERT INTO tb_date (DATE1, DATE2) VALUES 
	('2023-02-25',NOW());
INSERT INTO tb_date (DATE1) VALUES ('2023-02-27');



CREATE TABLE tb_string(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	str VARCHAR(30) NOT null
	str2 TEXT
);
DESC tb_string;

CREATE TABLE tb_string(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	str1 VARCHAR(30) NOT NULL,
	str text
	
);

DESC tb_string;


INSERT INTO tb_string (str1, str2) VALUES ('난 짧은글3', '난 엄청 긴글3');


SELECT * FROM tb_string;
SELECT * FROM tb_string WHERE idx=2;
SELECT * FROM tb_string WHERE idx=2 AND str1='난 짧은글2';
SELECT * FROM tb_string WHERE idx=2 AND str1='난 짧은글3';
SELECT * FROM tb_string WHERE idx=2 OR str1='난 짧은글3';

SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은%';
SELECT * FROM tb_string WHERE str1 LIKE '난 짧은';
SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은';
#4. 특수형
/*
enum : 여러 항목 중 1개만 선택할 수 있는 타입.
	HTML의 radio와 유사함.
set : 여러 항목 중 2개 이상을 선택할 수 있는 타입.
	checkbox와 유사함
*/
CREATE TABLE tb_spec (
	idx INT AUTO_INCREMENT,
	
	spec1 ENUM('M', 'W','T'),
	spec2 SET('A','B','C','D'),
	/* 아웃 라인 방식으로 컬럼을 먼저 생성한 후 별도로 기본키를 
	지정함*/
	
	PRIMARY KEY (idx)
);

INSERT INTO tb_spec (spec1, spec2) VALUE 
	('W', 'A,B,C'); #정상입력

INSERT INTO tb_spec (spec1, spec2) VALUE 
	('X', 'A,B,C'); #에러발생
INSERT INTO tb_spec (spec1, spec2) VALUE 
	('M', 'X,B,C'); #에러발생


/*
spec1 컬럼은 not null로 지정하지 않았으므로 null을 허용하는 
컬럼으로 정의된다. 따라서 값을 입력하지 않아도 된다.
*/
INSERT INTO tb_spec (spec2) VALUE ('B,C,D');
SELECT * FROM tb_spec;



# 파이썬 실습을 위한 테이블 생성
CREATE TABLE board
(
	num INT NOT NULL AUTO_INCREMENT, /* 일련번호. 자동증가컬럼. */
	title VARCHAR(100) NOT NULL, /* 제목 : 짧은 텍스트 */
	content TEXT NOT NULL,	/* 내용 : 긴 텍스트 */
	id VARCHAR(30) NOT NULL,
	postdate DATETIME DEFAULT CURRENT_TIMESTAMP, /* 작성일. 현재시간을
																디폴트 값으로 지정 */
	visitcount MEDIUMINT NOT NULL DEFAULT 0, /* 조회수 */
	PRIMARY KEY (num) 
);


#더미 데이터 입력
#특히 일련번호 컬럼은 쿼리문에서 생략한 상태로 작성한다.
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUE ('제목1', '내용1입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUE ('제목2', '내용2입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUE ('제목3', '내용3입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUE ('제목4', '내용4입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUE ('제목5', '내용5입니다','korea',NOW(),0);









