from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from .models import Comment
from .serializers import CommentSerializer, CommentListSerializer


# 코멘트 전체조회
@api_view(['GET'])
def comment_list(request):
    if request.method =='GET':
        CommentList = get_list_or_404(Comment)
        serializer = CommentListSerializer(CommentList,many=True)
        return Response(serializer.data)


# 특정 코멘트 조회 / 삭제 / 업데이트
@api_view(['GET','DELETE','PUT'])
def comment_detail(request,comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method=='GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    if request.method =='DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method =='PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


# userid가진 커멘트 전체조회 / 특정 커멘트 생성 
@api_view(['GET','POST'])
def comment_user(request,user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    # user의 모든 정보 조회
    if request.method =='GET':
        user_comment = get_list_or_404(Comment, user=user.id)
        serializer = CommentListSerializer(user_comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)            
    
    if request.method =='POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)