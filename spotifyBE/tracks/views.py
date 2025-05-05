from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from spotifyBE.tracks.models import Tracks
from spotifyBE.tracks.serializers import TracksSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from spotifyBE.utils.response import ApiResponse
from spotifyBE.relationships.serializers import ArtistTracksSerializer

class TracksViewSet(viewsets.ModelViewSet):
    """
    API endpoint cho phép CRUD các track
    """
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'lyrics']
    
    def create(self, request, *args, **kwargs):
        """
        Tạo một track mới với file upload
        """
        # Validate required fields
        required_fields = ['title', 'duration']
        for field in required_fields:
            if field not in request.data:
                return ApiResponse(
                    error=f'{field} is required',
                    statusCode=status.HTTP_400_BAD_REQUEST
                )
        
        # Xử lý file upload
        data = request.data.copy()
        
        # Thêm trường createdAt nếu chưa có
        if 'createdAt' not in data:
            data['createdAt'] = timezone.now()
            
        # Khởi tạo playCount là 0 nếu chưa có
        if 'playCount' not in data:
            data['playCount'] = 0
            
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return ApiResponse(
            data=serializer.data,
            statusCode=status.HTTP_201_CREATED
        )
    
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
        return ApiResponse(data=serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Lấy thông tin chi tiết của một track
        """
        instance = self.get_object()
        artist = instance.artists.all()
        serializerListArtist = ArtistTracksSerializer(artist, many=True)
        print(serializerListArtist.data)
        serializer = self.get_serializer(instance)
        dataResponse = serializer.data
        dataResponse['artists'] =[]
        # dataResponse['artists'] = serializerListArtist.data
        for tracrkartist in serializerListArtist.data:
            artist = {
                "artist" : tracrkartist['artist'],
                "owner" : tracrkartist['owner']
            }
            dataResponse['artists'].append(artist)

        return ApiResponse(data = dataResponse)
    
    def update(self, request, *args, **kwargs):
        """
        Cập nhật thông tin track với file upload
        """
        instance = self.get_object()
        data = request.data.copy()
        
        # Giữ nguyên file cũ nếu không có file mới được upload
        if 'track_file' not in data:
            data['track_file'] = instance.track_file
        if 'video_file' not in data:
            data['video_file'] = instance.video_file
        if 'image_file' not in data:
            data['image_file'] = instance.image_file
            
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return ApiResponse(data=serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        """
        Cập nhật một phần thông tin của một track
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return ApiResponse(data=serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        """
        Xóa một track
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return ApiResponse(
            data="Track deleted successfully",
            statusCode=status.HTTP_204_NO_CONTENT
        )
    
    @action(detail=True, methods=['post'])
    def increment_play_count(self, request, pk=None):
        """
        API endpoint để tăng số lần phát của một track
        """
        track = self.get_object()
        track.playCount += 1
        track.save()
        serializer = self.get_serializer(track)
        return ApiResponse(data=serializer.data)

    @action(detail=False, methods=['get'], url_path='search/(?P<query_string>[^/.]+)')
    def search(self, request, query_string=None): # Bỏ pk=None vì detail=False
       print("Từ khóa tìm kiếm:", query_string)
       tracks = Tracks.objects.filter(title__icontains=query_string)
       serializer = TracksSerializer(tracks, many=True)
       return ApiResponse(data=serializer.data)