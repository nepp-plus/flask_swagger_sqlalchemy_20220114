# 사용자에 관련된 기능을 수행하는 클래스.
# 메쏘드를 만들때, get / post / put / patch / delete로 만들면, 알아서 메쏘드로 세팅되도록.

from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger

from server.model import Users  # users 테이블에 연결할 클래스를 가져오기.

# 각 메쏘드별로 파라미터를 받아보자.

# post메쏘드에서 사용할 파라미터
post_parser = reqparse.RequestParser()  # post로 들어오는 파라미터를 확인해볼 변수
post_parser.add_argument('email', type=str, required=True, location='form') #파라미터 이름, 데이터 타입, 필수여부, 첨부된 곳
post_parser.add_argument('password', type=str, required=True, location='form')

# 회원가입에 사용할 4가지 파라미터 추가 / swagger를 통해서도 받아보자.
# put_parser / email, password, name, phone 4가지 변수.
# put 메쏘드에서 받아서 로그로만 출력
# swagger 문서 작업.

put_parser = reqparse.RequestParser()
put_parser.add_argument('email', type=str, required=True, location='form')
put_parser.add_argument('password', type=str, required=True, location='form')
put_parser.add_argument('name', type=str, required=True, location='form')
put_parser.add_argument('phone', type=str, required=True, location='form')

class User(Resource):
    
    @swagger.doc({
        'tags': ['user'],  # 어떤 종류의 기능인지 분류.
        'description': '사용자 정보 조회',
        'parameters': [
            # dict로 파라미터들 명시.
        ],
        'responses': {
            # 200일때의 응답 예시, 400일때의 예시 등.
            '200': {
                'description': '사용자 정보 조회 성공',
            },
            '400': {
                'description': '사용자 정보 조회 실패',
            }
        }
    })
    def get(self):
        """사용자 정보 조회"""
        return {
            "임시": "사용자 정보 조회"
        }
        
        
    @swagger.doc({
        'tags': ['user'],  # 어떤 종류의 기능인지 분류.
        'description': '로그인',
        'parameters': [
            {
                'name': 'email',
                'description': '로그인에 사용할 이메일',
                'in': 'formData', # query, formData 중 택일 (header 도 향후 사용)
                'type': 'string', # string, integer, number (float), boolean 중 택일 (향후 file 도 사용 예정),
                'required': True  # 필수 첨부 여부
            },
            {
                'name': 'password',
                'description': '로그인에 사용할 비밀번호',
                'in': 'formData', # query, formData 중 택일 (header 도 향후 사용)
                'type': 'string', # string, integer, number (float), boolean 중 택일 (향후 file 도 사용 예정),
                'required': True  # 필수 첨부 여부
            },
        ],
        'responses': {
            # 200일때의 응답 예시, 400일때의 예시 등.
            '200': {
                'description': '로그인 성공',
            },
            '400': {
                'description': '아이디 없는 상황',
            }
        }
    })
    def post(self):
        """로그인"""
        
        # 받아낸 파라미터들을 dict 변수에 담아두자.
        args = post_parser.parse_args()
        

        # email이 동일한 사람이 있는지? 찾아보자. (SELECT / WHERE 사용)
        
        login_user = Users.query.filter(Users.email == args['email']).first() # 쿼리 수행 결과중 첫 줄.
        
        # 일치하는 사람이 없다면? login_user 에 None이 대입됨.
        print('로그인 유져 : ', login_user)
        
        return {
            "임시": "로그인 기능"
        }
        
    @swagger.doc({
        'tags': ['user'],  # 어떤 종류의 기능인지 분류.
        'description': '회원가입',
        'parameters': [
            {
                'name': 'email',
                'description': '회원가입용 이메일 주소',
                'in': 'formData',
                'type': 'string',
                'required': True 
            },
            {
                'name': 'password',
                'description': '회원가입용 비밀번호',
                'in': 'formData',
                'type': 'string',
                'required': True 
            },
            {
                'name': 'name',
                'description': '사용자 본명',
                'in': 'formData',
                'type': 'string',
                'required': True 
            },
            {
                'name': 'phone',
                'description': '아이디찾기에 사용할 전화번호',
                'in': 'formData',
                'type': 'string',
                'required': True 
            },
        ],
        'responses': {
            # 200일때의 응답 예시, 400일때의 예시 등.
            '200': {
                'description': '회원가입 성공',
            },
            '400': {
                'description': '이메일 중복 가입 실패',
            }
        }
    })
    def put(self):
        """회원가입"""
        
        args = put_parser.parse_args()
        
        print(f"이메일 : {args['email']}")
        print(f"비밀번호 : {args['password']}")
        print(f"이름 : {args['name']}")
        print(f"전화번호 : {args['phone']}")
        
        return {
            "임시": "회원가입 기능"
        }