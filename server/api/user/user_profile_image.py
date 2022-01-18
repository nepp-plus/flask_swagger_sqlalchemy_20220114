import boto3

from flask import current_app
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage  # 파라미터로 파일을 받을때 필요한 클래스
from flask_restful_swagger_2 import swagger

put_parser = reqparse.RequestParser()
# 파일을 받는 파라미터는, FileStorage, files에서, 추가 행동 : append
put_parser.add_argument('profile_image', type=FileStorage, required=True, location='files', action='append')
put_parser.add_argument('user_id', type=int, required=True, location='form')

class UserProfileImage(Resource):
    
    @swagger.doc({
        'tags': ['user'],  # 어떤 종류의 기능인지 분류.
        'description': '사용자 프로필사진 등록',
        'parameters': [
            {
                'name': 'user_id',
                'description': '누구의 프사 등록?',
                'in': 'formData',
                'type': 'integer',
                'required': True
            },
            {
                'name': 'profile_image',
                'description': '실제로 첨부할 사진',
                'in': 'formData',
                'type': 'file',
                'required': True
            },
        ],
        'responses': {
            # 200일때의 응답 예시, 400일때의 예시 등.
            '200': {
                'description': '등록 성공',
            },
            '400': {
                'description': '등록 실패',
            }
        }
    })
    def put(self):
        """ 사용자 프로필사진 등록 """
        
        args = put_parser.parse_args()
        
        # aws - s3에, 어떤 키 / 비밀키를 들고갈지 세팅.
        # 키값들은 -> 환경설정에 저장해둔 값 불러와서 사용.
        aws_s3 = boto3.resource('s3',\
            aws_access_key_id= current_app.config['AWS_ACCESS_KEY_ID'],\
            aws_secret_access_key= current_app.config['AWS_SECRET_ACCESS_KEY'])
        
        # 파일의 경우 보통 여러장 첨부 가능.
        # args['profile_image'] 는 => list로 구성됨.
        
        for file in args['profile_image']:
            print(file) # file : 파일이름 / 실제 이미지등 본문 분리.
            
            # 파일 이름 저장됨 => S3 버킷에 저장될 경로 생성에 활용.
            print(file.filename)
            s3_file_path = f'images/profile_imgs/{file.filename}'  # 올라갈 경로
            
            # 파일 본문도 따로 저장. => 실제로 S3 경로에 업로드.
            file_body = file.stream.read() # 올려줄 파일
        
        return {
            '임시': '사용자 프사 등록 기능'
        }