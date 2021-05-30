import json
import subprocess

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
@api_view(['POST'])
def scan_image_klar(request):
    if request.method == 'POST':
        data = request.data
        host = data['host']
        port = data['port']
        username = data['username']
        password = data['password']
        klar_path = data['klar_path']
        docker_image = data['docker_image']
        command = '''CLAIR_ADDR=http://postgres@{}:{} JSON_OUTPUT=1 DOCKER_USER={} DOCKER_PASSWORD={} {} {}'''.format(host, port, username, password, klar_path, docker_image)
        child = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        response, error = child.communicate()
        value = {}
        try:
            value = json.dumps(json.loads(response), sort_keys=True, indent=4, ensure_ascii=False)
        except ObjectDoesNotExist:
            pass
        finally:
            context = {
                'command': command,
                'response': value,
                'error': error.decode(encoding='utf-8', errors='ignore').strip()
            }
            return Response(context, status=status.HTTP_200_OK)
