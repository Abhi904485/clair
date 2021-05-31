from django.shortcuts import render
from django.db import connection
from django.contrib import messages


# Create your views here.
def raw_query(request):
    context = {}
    if request.method == "POST":
        query = request.POST['raw_query']
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                columns = [col[0] for col in cursor.description]
                rows = [row for row in cursor.fetchall()]
                context = {
                    'columns': columns,
                    'rows': rows,
                    'query': query
                }
                messages.success(request, "Query {} Executed Successfully".format(query))
            return render(request, 'raw_query.html', context=context)
        except Exception as e:
            messages.error(request, "{}".format(e.args[0]))
            context.update({'query': query})
            return render(request, 'raw_query.html', context=context)
    else:
        context.update({'query': """Select v.name as v_name ,  v.link as v_link , v.severity as v_severity ,  v.created_at as v_created_at,  v.severity_source ,  n.name , n.version_format from vulnerability v INNER JOIN namespace n on n.id = v.namespace_id LIMIT 100"""})
        return render(request, 'raw_query.html', context=context)