import boto3
import time
import os
import hashlib # str -> 암호화된 문구로 변경.

from flask import current_app
from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger
from werkzeug.datastructures import FileStorage

from server import db
from server.model import Feeds, Users

post_parser = reqparse.RequestParser()
post_parser.add_argument('user_id', type=int, required=True, location='form')
post_parser.add_argument('lecture_id', type=int, required=True, location='form')
post_parser.add_argument('content', type=str, required=True, location='form')
post_parser.add_argument('feed_images', type=FileStorage, required=False, location='files', action='append')

class Feed(Resource):
    
    @swagger.doc({
        'tags': ['feed'],
        'description': '게시글 등록하기',
        'parameters': [
            {
                'name': 'user_id',
                'description': '어느 사용자가 쓴건지',
                'in': 'formData',
                'type': 'integer',
                'required': True
            },
            {
                'name': 'lecture_id',
                'description': '어느 강의에 대해 쓴건지',
                'in': 'formData',
                'type': 'integer',
                'required': True
            },
            {
                'name': 'content',
                'description': '게시글 내용',
                'in': 'formData',
                'type': 'string',
                'required': True
            },
        ],
        'responses': {
            '200': {
                'description': '게시글 등록 성공',
            },
            '400': {
                'description': '등록 실패',
            }
        }
    })
    def post(self):
        """ 게시글 등록하기 """
        
        args = post_parser.parse_args()
        
        new_feed = Feeds()
        new_feed.user_id = args['user_id']
        new_feed.lecture_id = args['lecture_id']
        new_feed.content = args['content']
        
        db.session.add(new_feed)
        db.session.commit()
        
        # commit시점 이후에는, DB에 등록 완료 -> new_feed의 id / created_at 등의 자동 등록 데이터도 모두 설정 완료.
        
        # 사진 목록을 등록하는 행위는 commit()으로 id값이 확인 가능하게 된 후에 작업하자.
        
        # 사진이 첨부되지 않았을 수도 있다. => 확인해보고 올리자.
        
        if args['feed_images']:   # 사진이 파라미터에 첨부되었나?
            
            # 1. 사용자 누구?
            upload_user = Users.query.filter(Users.id == args['user_id']).first()
            
            # 2. AWS 접속 도구
            aws_s3 = boto3.resource('s3',\
                aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],\
                aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'])
            
            for image in args['feed_images']:
                # 첨부된 사진들을 AWS S3에 올려주기.
                
                # 1. 파일이름 (중복회피) 재가공
                # 사용자id 암호화, 현재시간 숫자로.
                s3_file_name = f"images/feed_images/MySNS_{사용자id암호화}_{현재시간숫자}{.확장자}"
                
                # 2. aws s3에 파일 업로드
                
                # feed_images 테이블에, 이 게시글의 사진으로 S3사진 주소 등록.
                pass
        
        return {
            'code': 200,
            'message': '게시글 등록 성공',
            'data': {
                'feed': new_feed.get_data_object()
            }
        }
    
    @swagger.doc({
        'tags': ['feed'],
        'description': '게시글 목록 조회',
        'parameters': [
            
        ],
        'responses': {
            '200': {
                'description': '게시글 목록 조회',
            },
            '400': {
                'description': '조회 실패',
            }
        }
    })
    def get(self):
        """ 모든 게시글 최신순 조회 """
        
        # 모든 게시글 -> 생성일시 역순으로 -> 최신순. (SQL : ORDER BY + DESC => ORM으로?)
        feed_data_arr = Feeds.query.order_by(Feeds.created_at.desc()).all()
        
        feeds = [ row.get_data_object()  for row in feed_data_arr ]
        
        return {
            'code': 200,
            'message': '모든 게시글 조회',
            'data': {
                'feeds': feeds
            }
        }