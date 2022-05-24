from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.stories import Story
from ..serializers import StorySerializer

# Create your views here.
class Stories(generics.ListCreateAPIView):
    """stop it"""
    permission_classes=(IsAuthenticated,)
    serializer_class = StorySerializer
    def get(self, request):
        """Index request"""
        # Get all the stories:
        # stories = Story.objects.all()
        # Filter the stories by owner, so you can only see your owned stories
        stories = Story.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = StorySerializer(stories, many=True).data
        return Response({ 'stories': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['story']['owner'] = request.user.id
        # Serialize/create story
        story = StorySerializer(data=request.data['story'])
        # If the story data is valid according to our serializer...
        if story.is_valid():
            # Save the created story & send a response
            story.save()
            return Response({ 'story': story.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(story.errors, status=status.HTTP_400_BAD_REQUEST)

class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """stop it"""
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the story to show
        story = get_object_or_404(Story, pk=pk)
        # Only want to show owned stories?
        if request.user != story.owner:
            raise PermissionDenied('Unauthorized, you do not own this story')

        # Run the data through the serializer so it's formatted
        data = StorySerializer(story).data
        return Response({ 'story': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate story to delete
        story = get_object_or_404(Story, pk=pk)
        # Check the story's owner against the user making this request
        if request.user != story.owner:
            raise PermissionDenied('Unauthorized, you do not own this story')
        # Only delete if the user owns the  story
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Story
        # get_object_or_404 returns a object representation of our Story
        story = get_object_or_404(Story, pk=pk)
        # Check the story's owner against the user making this request
        if request.user != story.owner:
            raise PermissionDenied('Unauthorized, you do not own this story')

        # Ensure the owner field is set to the current user's ID
        request.data['story']['owner'] = request.user.id
        # Validate updates with serializer
        data = StorySerializer(story, data=request.data['story'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
