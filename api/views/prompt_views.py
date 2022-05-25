from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.prompts import Prompt
from ..serializers import PromptSerializer

# Create your views here.
class Prompts(generics.ListCreateAPIView):
    """stop it"""
    permission_classes=(IsAuthenticated,)
    serializer_class = PromptSerializer
    def get(self, request):
        """Index request"""
        # Get all the stories:
        # prompts = Prompt.objects.all()
        # Filter the prompts by owner, so you can only see your owned prompts
        prompts = Prompt.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = PromptSerializer(prompts, many=True).data
        return Response({ 'prompts': data })
    def get(self, request):
      """Index request"""
      # Get all the stories:
      # prompts = Prompt.objects.all()
      # Filter the prompts by owner, so you can only see your owned prompts
      prompts = Prompt.objects.filter(is_active=True)
      # Run the data through the serializer
      data = PromptSerializer(prompts, many=True).data
      return Response({ 'prompts': data })

    def post(self, request):
        """Create request"""
        print(request.data)
        # Add user to request data object
        request.data['prompt']['owner'] = request.user.id
        # Serialize/create prompt
        prompt = PromptSerializer(data=request.data['prompt'])
        # If the prompt data is valid according to our serializer...
        if prompt.is_valid():
           # Save the created prompt & send a response
            prompt.save()
            return Response({ 'prompt': prompt.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(prompt.errors, status=status.HTTP_400_BAD_REQUEST)

class PromptDetail(generics.RetrieveUpdateDestroyAPIView):
    """stop it"""
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the prompt to show
        prompt = get_object_or_404(Prompt, pk=pk)
        # Only want to show owned stories?
        if request.user != prompt.owner:
            raise PermissionDenied('Unauthorized, you do not own this prompt')

        # Run the data through the serializer so it's formatted
        data = PromptSerializer(prompt).data
        return Response({ 'prompt': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate prompt to delete
        prompt = get_object_or_404(Prompt, pk=pk)
        # Check the prompts's owner against the user making this request
        if request.user != prompt.owner:
            raise PermissionDenied('Unauthorized, you do not own this prompt')
        # Only delete if the user owns the  prompt
    def partial_update(self, request, pk):
        """Update Request"""
        # Locate prompt
        # get_object_or_404 returns a object representation of our prompt
        prompt = get_object_or_404(Prompt, pk=pk)
        # Check the prompts's owner against the user making this request
        if request.user != prompt.owner:
            raise PermissionDenied('Unauthorized, you do not own this prompt')

        # Ensure the owner field is set to the current user's ID
        request.data['prompt']['owner'] = request.user.id
        # Validate updates with serializer
        data = PromptSerializer(prompt, data=request.data['prompt'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
