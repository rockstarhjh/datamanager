
from django.contrib import messages
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework_datatables.filters import DatatablesFilterBackend

from company.filters import ComFilter
from .form import ComForm
from .models import Company
from .serializers import ComSerializer
from rest_framework import viewsets, renderers, status, generics, filters


# Create your views here.
class ComModelViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = ComSerializer
    # permission_classes = (IsAdminUser,)
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'ceo', 'address']
    filter_backends = [DjangoFilterBackend, DatatablesFilterBackend]
    # search_fields = ['name']
    filterset_class = ComFilter


# class ComDetail(APIView):
#
#     def get(self):


class ComViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = ComSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        #
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(queryset, many=True)

        form = ComForm()
        return Response({'form': form}, template_name='company/company.html')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        form = ComForm()
        headers = self.get_success_headers(serializer.data)
        messages.info(request, '등록되었습니다.')
        return redirect('company:com-list')
        # return Response({'data': serializer.data, 'form': form}, status=status.HTTP_201_CREATED, headers=headers,
        #             template_name='company/company.html')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # print("get")
        # query = request.GET.get('query', None)  # read extra data
        # print(self.serializer_class(instance).data['name'])
        data = self.serializer_class(instance).data
        # print(data)
        form = ComForm(data)
        return Response({'data': data, 'form': form}, template_name='company/comForm.html')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # print('업데이트')
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        form = ComForm(serializer.data)
        messages.info(request, '수정되었습니다.')
        return Response({'data': serializer.data, 'form': form}, template_name='company/comForm.html')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        # print(instance.delete())
        # return HttpResponseRedirect(redirect_to='https://google.com')
        return Response({'status': True})


class ComList(generics.ListAPIView):
    serializer_class = ComSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name']

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases for
    #     the user as determined by the username portion of the URL.
    #     """
    #
    #     name = self.kwargs['name']
    #     print('1')
    #     print(name)
    #     test = Company.objects.filter(name__icontains=name)
    #     print(test[0].name)
    #     return Company.objects.filter(name__icontains=name)
