from flask import request, json, Response, Blueprint

defect_api = Blueprint('defect_api', __name__)

@defect_api.route('/', methods=['GET'])
def get_all():
    defects = [
        {
            "name": "loose hold",
            "date": "05-05-2019",
            "section": "4",
            "route": "climbHard"
        }
    ]
    return custom_response(defects, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )