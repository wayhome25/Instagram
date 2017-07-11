# 인스타그램st  웹어플리케이션 구현
> 인스타그램 기능을 가진 웹어플리케이션을 구현하며 Django를 학습합니다.

## 결과물
- [배포 사이트 바로가기](http://instagram-practice.tk/)
- [Microsoft Azure](https://azure.microsoft.com/ko-kr/?&wt.mc_id=AID623284_SEM_ANFOP6Xj) 를 활용하여 배포

## 목표

1. 동작하는 단위별로 commit을 추가한다. 코드 리뷰를 고려한 commit 메시지를 작성한다. (지금까지의 [commit 이력](https://github.com/wayhome25/Instagram/commits/master))
2. 필요한건 [Django 공식 문서](https://docs.djangoproject.com/en/1.11/), stackoverflow를 찾아보고 문제를 해결한다.
3. 궁금한 코드는 [Django 소스코드](https://github.com/django/django/tree/1.10.6/django) 를 열어서 직접 읽어본다.
4. 능동적으로 고민하고 가능한 스스로 코드를 짜본다. 비효율적이라도 직접 해보고, 다른 사람의 코드를 참고한다.


## 공부한 부분
> 구현 중 새롭게 알게된 것, 유용하다고 생각한 부분들을 블로그에 정리합니다.

- [쿼리셋 수정을 통한 웹서비스 성능 개선 - select_related, prefetch_related](https://wayhome25.github.io/django/2017/06/20/selected_related_prefetch_related/)
- [사용자 정의 필터 (Custom Template Filter)를 활용하여 해시태그 링크 구현하기](https://wayhome25.github.io/django/2017/06/22/custom-template-filter/)
- [Ajax / jQuery를 활용하여 새로고침 없이 좋아요 기능 구현하기](https://wayhome25.github.io/django/2017/06/25/django-ajax-like-button/)
- [django-imagekit를 활용하여 유저가 업로드한 이미지를 수정](https://wayhome25.github.io/django/2017/05/11/image-thumbnail/)

## 연습내용
- Django
  - 다양한 Model Relationship 활용 - 1:1, 1:N, M:N(through)
  - [쿼리셋 최적화](https://wayhome25.github.io/django/2017/06/20/selected_related_prefetch_related/) - 중복 DB쿼리 최소화 (select_related, prefetch_related, Django debug toolbar 활용)
  - django-allauth 를 활용한 Facebook 로그인 기능
  - [사용자 정의 필터](https://wayhome25.github.io/django/2017/06/22/custom-template-filter/) - 해시태그 링크 구현
  - [django-imagekit](https://wayhome25.github.io/django/2017/05/11/image-thumbnail/) - 유저 업로드 media파일 관리
- 프론트엔드
  - [Ajax](https://wayhome25.github.io/django/2017/06/25/django-ajax-like-button/) 서버 비동기 통신 - 무한스크롤, 댓글, 좋아요 추가
  - SASS, JavaScript, jQuery, Bootstrap grid system 활용    
- 배포
  - Microsoft Azure 를 활용한 배포 연습
  - AWS Elastic Beanstalk를 활용한 배포 연습
  - [sentry](https://sentry.io) - 배포 후 에러로깅
  - PostgreSQL 연동
  - 실행 환경에 따른 (개발/배포) requirements.txt, settings.py 파일 분리
  - SECRET_KEY 설정 분리 (환경변수패턴 / 비밀파일패턴)
- 그 밖의 [연습과정 TIL 기록](https://wayhome25.github.io/#til-today-i-learned)
