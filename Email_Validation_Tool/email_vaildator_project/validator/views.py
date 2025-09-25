from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import asyncio
import nest_asyncio
from .async_validation import validate_emails_batch


class EmailValidationView(APIView):
    def post(self, request):
        emails = request.data.get("emails", [])
        if not emails or not isinstance(emails, list):
            return Response(
                {"error": "Please provide a list of emails in the 'emails' field."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        nest_asyncio.apply()

        try:
            results = asyncio.run(validate_emails_batch(emails))
        except Exception as e:
            return Response(
                {"error": f"An error occurred while validating emails: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(results, status=status.HTTP_200_OK)
