from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage  # 파라미터로 파일을 받을때 필요한 클래스

put_parser = reqparse.RequestParser()
# 파일을 받는 파라미터는, FileStorage, files에서, 추가 행동 : append
put_parser.add_argument('profile_image', type=FileStorage, required=True, location='files', action='append')
put_parser.add_argument('user_id', type=int, required=True, location='form')

class UserProfileImage(Resource):
    
    def put(self):
        return {
            '임시': '사용자 프사 등록 기능'
        }