from rest_framework.views import APIView

class AdvocatesDetail(APIView):
    
    def get_object(self, username):
        try:
            return Advocates.objects.get(username=username)

        except Advocates.DoesNotExist:
            # raise Advocates
            raise Http404

    def get(self, request, username):
        # advocate = Advocates.objects.get(username=username)
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
        # return Response('username')

    def put(self, request, username):
        # advocate = Advocates.objects.get(username=username)
        advocate = self.get_object(username)
        advocate.username = request.data['username']
        advocate.name = request.data['name']
        advocate.save()
        print('data updated')

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        # advocate = Advocates.objects.get(username=username)
        advocate = self.get_object(username)
        advocate.delete()
        print('data deleted')
        return Response('User '+ str(advocate.username) +' was deleted')