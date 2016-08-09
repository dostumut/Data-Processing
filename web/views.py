from celery.result import AsyncResult
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from web.tasks import do_amount_of_events_per_application_calculation
from web.tasks import do_product_launched_calculation


@csrf_exempt
def run_amount_of_events_per_application(request):
    job = do_amount_of_events_per_application_calculation.delay()
    return JsonResponse({'job_id': job.id})

@csrf_exempt
def run_amount_of_launch(request):
    job = do_product_launched_calculation.delay()
    return JsonResponse({'job_id': job.id})


def poll_state(request):
    """ A view to report the progress to the user """
    if 'job_id' in request.GET:
        job_id = request.GET['job_id']
    else:
        return HttpResponse('No job id given.')

    job = AsyncResult(job_id)
    if job.state is 'SUCCESS':
        return JsonResponse({'state': job.state})

    return JsonResponse({'state': job.state, 'result': job.result})


def amount_of_events_result(request):
    if 'job_id' in request.GET:
        job_id = request.GET['job_id']
    else:
        return HttpResponse('No job id given.')

    job = AsyncResult(job_id)
    return render(request, "amount_of_events_result.html", {'applications': job.result})


def amount_of_launch_result(request):
    if 'job_id' in request.GET:
        job_id = request.GET['job_id']
    else:
        return HttpResponse('No job id given.')

    job = AsyncResult(job_id)
    return render(request, "amount_of_launch.html", {'applications': job.result})


def calculations(request):
    return render(request, 'calculations.html')


def visualization(request):
    return render(request, 'visualization.html')
