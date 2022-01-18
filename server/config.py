# 플라스크에 적용 가능한 환경설정 모아두는 클래스
"""
Flask Configuration
"""

class Config(object):
    DEBUG = False
    TESTING = False
    
    # SQLAlchemy가 접속할 DB 연결 정보 (URI)
    # SQLAlchemy 라이브러리가, 어떤 변수를 끌어다 쓸지도 미리 지정되어있음. => 변수이름 바꾸면 안됨.
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://아이디:비밀번호@DB호스트주소/논리DB이름"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:Vmfhwprxm!123"+\
                            "@finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com/my_sns_ckj"
    
    # DB 변경 추적 기능 꺼두기
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # S3 접속 정보들을 변수들로 저장
    AWS_ACCESS_KEY_ID = 'AKIAYEL64SLYIIYVDTUZ'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_S3_BUCKET_NAME = 'neppplus.python.202201.ckj' # 어느 저장소에 저장할건지. 이름
    
class ProductionConfig(Config):
    # 기본 설정 그대로. 실 서버에서도.
    pass

class TestConfig(Config):
    TESTING = True  # 테스팅 환경이 맞다고 설정.
    
class DebugConfig(Config):
    DEBUG = True # 개발모드가 맞다고 설정.