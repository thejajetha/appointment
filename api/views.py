from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from api.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication,permissions
from api.models import Appointment
from api.serializer import AppointmentSerializer
from api.permissions import IsOwnerOnly 
from datetime import datetime
# Create your views here.


class SignUpView(APIView):

    def post(self,request,*args,**kwargs):

        serializer_instance=UserSerializer(data=request.data)   #deserialization

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        
        else:

            return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


# class SignUpView(CreateAPIView):

#     serializer_class=UserSerializer



class AppointmentListCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        qs=Appointment.objects.filter(customer=request.user).order_by('-date')

        serializer_instance=AppointmentSerializer(qs,many=True)

        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):

        serializer_instance=AppointmentSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(customer=request.user)

            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        
        else:

            return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class AppointmentRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=AppointmentSerializer

    queryset=Appointment.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsOwnerOnly]

    # def get(self,request,*args,**kwargs):

    #     id=kwargs.get('pk')

    #     appointment_object=get_object_or_404(Appointment,id=id)

    #     self.check_object_permissions(request,appointment_object)

    #     serializer_instance=AppointmentSerializer(appointment_object,many=False)

    #     return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    
    # def patch(self,request,*args,**kwargs):

    #     id=kwargs.get('pk')

    #     appointment_object=get_object_or_404(Appointment,id=id)

    #     self.check_object_permissions(request,appointment_object)

    #     serializer_instance=AppointmentSerializer(data=request.data,instance=appointment_object)

    #     if serializer_instance.is_valid():

    #         serializer_instance.save()

    #         return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
    
    #     else:

    #         return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
        
    # def delete(self,request,*args,**kwargs):

    #     id=kwargs.get('pk')

    #     appointment_object=get_object_or_404(Appointment,id=id)

    #     self.check_object_permissions(request,appointment_object)

    #     appointment_object.delete()

    #     return Response(data={"message:deleted"},status=status.HTTP_202_ACCEPTED)
    

class AvailableSlotList(APIView):

    def get(self,request,*args,**kwargs):

        date_str=request.query_params.get('date')

        date_obj=datetime.strptime(date_str,'%Y-%m-%d').date()

        all_slots=dict(Appointment.TIME_SLOT_CHOICES)

        booked_slots=Appointment.objects.filter(date=date_obj).values_list('time_slot',flat=True)

        free_slots=[

            {'slot_id':slot_id,'slot_display':slot_display}

            for slot_id,slot_display in all_slots.items()

            if slot_id not in booked_slots
        ]

        return Response(data=free_slots)











        
    
        