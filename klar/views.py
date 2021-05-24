import json
import subprocess
import os
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


def set_docker_username_password():
    subprocess.Popen('aws ecr get-login-password --region {} --profile {}'.format('ap-south-1', 'nanosec'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
    os.environ['DOCKER_USER'] = "AWS"
    os.environ['DOCKER_PASSWORD'] = 'eyJwYXlsb2FkIjoiSGZ0SjNxZEFVQWtXQzNDcmtRQ1hEa0JjUEsrWWlrZmtWbkswVE9HTFAzM1JOWnhUckdDR2lDVk4zTmYzd1I2SjVGdVFUOFVHL2lWdEgvZFNzUlVmalExaWlKZzRHNEdjU1pKcjZaZEZzUzlpOVZoWmZmWVd0RmFrQTRobnkzLzdaVnZLTmpFK1VocmlSVGN4dEpUQThSZWVVT0V2eExqS1E2V1hMODZ5aEdSQUNZTVlzRTE1UG9GNUkrSC8wT1RLTEpZWkFFWkRTcWFndHU2amdGaU9XUUlERHBMS1V3cWF5dXEzUkdLSW9qdVQ5cEppNndRempsdjI3M3dqanJuNWJvQ1hZRFgzdHMwUDdkQXphQWY0bjdxNE1xcmpleXJ6a1I2RDZFUzN6WklYY0tMQkNRTVZNV08wL0JlWi8rWld1c0k2L1BSbFpnZ2ZzaTBmQVJ4R3VhOGJtM2psRElQZi84Z3JEWWpETWRQbEIxdFR4U0E5UnJjRHdVMGxkcVF1a0RGRWZTWm1JVC9BNkVvVTVzcHJTR0RRR2ErOXYwSkVFM0ZsbitQdm1PbVM5YVhab1R6OXhSZnFHRksxYTJVSEI1U2VjbTgxaHIrTDhYOGEzN1U4NVF1VE5kbWpPc3llakVYbkptUjdZNHJ5MjMxaDI1ME1CZGZOUVZMOEZ1TWVHTFpLUCtpMXdwaU8zQXJ6bEI4M0dzL09UcXNnb3JieDBXZFcyT2tjalRxWjVTeDNpTGcwVXdHSS92NUxnaDd3dHNEZUdBTGRENkl2SGswOTlOTjdKcG5iVnJ1SUF3QWJOdy92Y3l4dzVkcXJXOHdGcUw2S1R2OXZkZVkzUWR0VUVlK1RaYk1lb2p5emMvL2lHaXFEQTV3V2JzUHhFODNrcjNrdEo3SDZlQUZ5VGFoWnRFU2M5bGhSaDZkOW5aeENxRkR6dEJ4R0NtTUlmZVdpRWFkb29UOExxakN2UU9oMW5xSUdUdlkvYnMxYXJldGxjdXRWck5idVJ5VWh0R1l3YnBWdTFpL2lldGFSajV6MXlmVnFIOG81V244ZlVZQ3ZGalRpUS9vVHZ6cndCZURidXFsUXJJeklmSEwxT2dtc3hPNzNvQUtIYjJ6dmhSOEFjQ3NReDk2TUZ5NHhFSVR3cWdiYXZaaGJxd3M5NjNRalRBcXYrTGIyR1RzOXhOeFZDZGtpcDNqSnE5WGxKc2xFTjBjRnpyTkROZVZVd0tFZjNFLzBOc0doaUQzc1UyTm15M0dIWU01KzBaTkkvbzh3N3Z6endMTUpUVTk1clJRUlZkaktiMlp2WFlpWllEYmJNcktUbWloVmVTM2tGdGQ5ZWthcG5idi9vR3puS0tyQTM4VjlXYkF1UjdsVzFOS3lQM1VSV2hEeTVtdHBuT0Q1eTQrcHN5bUlDWHpjSlZEcEtlTVpiZmx2emFmVnh2blZyYStNMXQ2d0RpWmlFemlDelE9PSIsImRhdGFrZXkiOiJBUUlCQUhpSFdhWVRuUlVXQ2Jueis3THZNRytBUHZUSHpIbEJVUTlGcUVtVjI2QmR3d0cyRFViTmdxOU1CZnd4WjJKV1ZvWERBQUFBZmpCOEJna3Foa2lHOXcwQkJ3YWdiekJ0QWdFQU1HZ0dDU3FHU0liM0RRRUhBVEFlQmdsZ2hrZ0JaUU1FQVM0d0VRUU1kT21hemc2L3pJbkZoOVdDQWdFUWdEdUNVOG1yQ21uQUg3OThmSnlDZHZVbjV5RkRmYXpaSnlod2VYT2l2VHJjK0ljSElXUnd1bTRDUTl4WUkvS0tUWVA4cldhdDBURnZNcjJ0WUE9PSIsInZlcnNpb24iOiIyIiwidHlwZSI6IkRBVEFfS0VZIiwiZXhwaXJhdGlvbiI6MTYyMTkwNzM5NH0='


# Create your views here.
def scan_image(request):
    context = {}
    if request.method == "POST":
        nlb_host = request.POST['nlb_host']
        nlb_port = request.POST['clair_port']
        docker_username = request.POST['username']
        docker_password = request.POST['password']
        # set_docker_username_password()
        # docker_username = os.environ.get('DOCKER_USER')
        # docker_password = os.environ.get('DOCKER_PASSWORD')
        klar_uploaded_file = request.FILES['klar_binary_path']
        fs = FileSystemStorage()
        filename = fs.save(klar_uploaded_file.name, klar_uploaded_file)
        binary_save_location = os.path.join(fs.location, filename)
        os.system("chmod +x {}".format(binary_save_location))
        docker_image = request.POST['docker_image']
        command = '''CLAIR_ADDR=http://postgres@{}:{} JSON_OUTPUT=1 DOCKER_USER={} DOCKER_PASSWORD={} {} {}'''.format(nlb_host, nlb_port, docker_username, docker_password, binary_save_location, docker_image)
        messages.info(request, 'image {} scanning is in progress via klar binary path {} do not refresh page'.format(docker_image, binary_save_location))
        child = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        response, error = child.communicate()
        value = {}
        try:
            value = json.dumps(json.loads(response), sort_keys=True, indent=2, ensure_ascii=False)
            messages.success(request, 'image {} scanning was Successful!'.format(docker_image))
        except ObjectDoesNotExist:
            messages.error(request, 'image {} scanning was Failed!'.format(docker_image))
        finally:
            context = {
                'command': command,
                'response': value,
                'error': error.decode(encoding='utf-8', errors='ignore').strip()
            }
            return render(request, 'klar/klar.html', context=context)
    else:
        return render(request, 'klar/klar.html', context=context)
