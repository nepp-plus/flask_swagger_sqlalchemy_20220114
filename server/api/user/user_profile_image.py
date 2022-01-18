from flask_restful import Resource

class UserProfileImage(Resource):
    
    def put(self):
        return {
            '임시': '사용자 프사 등록 기능'
        }