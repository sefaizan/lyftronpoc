from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from databaseconnection.models import Integration
import json


def get_mysql_credentials(sql_dialect, source):
    if sql_dialect.name.lower() == 'mysql':
        str_creds = source.credential
        creds = json.loads(str_creds)
        host = creds['host']
        port = creds['port']
        user = creds['user']
        password = creds['password']
        return host, port, user, password

def get_mysql_metadata(integration):
    host, port, user, password = get_mysql_credentials(integration.source.sql_dialect, integration.source)
    a = 1
    # your code will be here for fetching metadata
    pass

class ListMetaData(APIView):
    
    def get(self, request, format=None):
        integration_id = request.data.get('integration', None)
        if not integration_id:
            return Response(data={'error': 'Please provide integration ID'})
        integration = Integration.objects.filter(pk=integration_id)
        if not integration:
            return Response(data={'error': 'Integration not found'})
        integration = integration[0]
        metadata = get_mysql_metadata(integration)
        return Response(data={'data': 'integration found'})
