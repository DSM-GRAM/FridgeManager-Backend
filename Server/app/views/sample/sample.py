from flasgger import swag_from
from flask import request

from app.docs.sample import *
from app.views import BaseResource
from flask_validation import validate_keys

from app.models.sample import SampleM


class Sample(BaseResource):
    @swag_from(SAMPLE_POST)
    @validate_keys(('age', 'name'))
    def post(self):
        payload = request.json

        return self.unicode_safe_json_dumps(payload, 201)


class PostSample(BaseResource):
    def post(self):
        SampleM(id=request.json['id'], pw=request.json['pw']).save()

        return '', 201
