from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from .models import Cat, Target, Mission
from .serializers import CatSerializer, TargetSerializer, MissionSerializer
from rest_framework.response import Response
from rest_framework import status

#Cats
#creates cat view 
class CatCreateView(ListCreateAPIView):
        queryset = Cat.objects.all()
        serializer_class = CatSerializer


# delete cat by pk
class CatDeleteView(DestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    lookup_field = 'id'

#get - get all cats
class CatListView(ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

# put - update salary
class CatUpdateView(UpdateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    lookup_field = 'id'

    def partial_update(self, request, *args, **kwargs):
        catins = self.get_object()
        add_salary = request.data.get('salary')
        if add_salary is None:
            return Response(
                {"error": "There is no salary field in request"},
                status=status.HTTP_400_BAD_REQUEST)
        catins.salary += int(add_salary)
        catins.save()
        return Response({
                "message": f"Salary updated!",
                "updated_salary": catins.salary,},
            status=status.HTTP_200_OK,)
    

# get by pk - single cat
class CatDetailView(RetrieveAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    lookup_field = 'id'
     
    


#Mission views
#get missions
class MissionsListView(ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


