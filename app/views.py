from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Course, Student, Mentor
from .serializer import CourseSerializer, StudentSerializer, MentorSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentListCreateAPIView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrieveAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MentorListCreateAPIView(APIView):

    def get(self, request, *args, **kwargs):
        mentors = Mentor.objects.all()
        serializer = MentorSerializer(mentors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorRetrieveUpdateDestroyAPIView(APIView):
    def get_mentor(self, mentor_id):
        return generics.get_object_or_404(Mentor, id=mentor_id)

    def get(self, request, mentor_id, *args, **kwargs):
        serializer = MentorSerializer(self.get_mentor(mentor_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, mentor_id, *args, **kwargs):
        serializer = MentorSerializer(self.get_mentor(mentor_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, mentor_id, *args, **kwargs):
        self.get_mentor(mentor_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
