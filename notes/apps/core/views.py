from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "pages":[
            {
                "is_active": True,
                "value": "Python",
                "id": "collapseExample1",
                "href": "#collapseExample1",
                "sub_pages": [
                    {
                        "is_active": False,
                        "value": "Pandas",
                        "id": "collapseExample4",
                        "href": "#collapseExample4"
                    },
                    {
                        "is_active": True,
                        "value": "Django",
                        "id": "collapseExample5",
                        "href": "#collapseExample5"
                    },
                ],
            },
            {
                "is_active": False,
                "value": "Docker",
                "id": "collapseExample2",
                "href": "#collapseExample2",
                "sub_pages": [
                    {
                        "is_active": False,
                        "value": "Ejemplo",
                        "id": "collapseExample5",
                        "href": "#collapseExample5"
                    }
                ]
            },
            {"is_active": False,
            "value": "AWS",
            "id": "collapseExample3",
            "href": "#collapseExample3",
            "sub_pages": []},
        ]
    }
    return render(request, "core/index.html", context)