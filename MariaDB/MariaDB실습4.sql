
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
	(title, content, id, postdate, vistcount)
VALUE ('제목1', '내용1입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, vistcount)
VALUE ('제목2', '내용2입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, vistcount)
VALUE ('제목3', '내용3입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, vistcount)
VALUE ('제목4', '내용4입니다','korea',NOW(),0);
INSERT INTO board
	(title, content, id, postdate, vistcount)
VALUE ('제목5', '내용5입니다','korea',NOW(),0);