from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from spotifyBE.tracks.models import Tracks
from spotifyBE.tracks.serializers import TracksSerializer

class TracksViewSet(viewsets.ModelViewSet):
    """
    API endpoint cho phép CRUD các track
    """
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer
    
    def create(self, request, *args, **kwargs):
        """
        Tạo một track mới
        """
        # Thêm trường createdAt nếu chưa có
        if 'createdAt' not in request.data:
            request.data['createdAt'] = timezone.now()
            
        # Khởi tạo playCount là 0 nếu chưa có
        if 'playCount' not in request.data:
            request.data['playCount'] = 0
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def list(self, request, *args, **kwargs):
        """
        Lấy danh sách tất cả các track
        """
        queryset = self.filter_queryset(self.get_queryset())
        
        # Kiểm tra nếu có tham số tìm kiếm theo title
        title = request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
            
        # Kiểm tra status nếu có
        status_param = request.query_params.get('status', None)
        if status_param:
            queryset = queryset.filter(status=status_param)
            
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Lấy thông tin chi tiết của một track
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        """
        Cập nhật toàn bộ thông tin của một track
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        """
        Cập nhật một phần thông tin của một track
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        """
        Xóa một track
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['post'])
    def increment_play_count(self, request, pk=None):
        """
        API endpoint để tăng số lần phát của một track
        """
        track = self.get_object()
        track.playCount += 1
        track.save()
        serializer = self.get_serializer(track)
        return Response(serializer.data)