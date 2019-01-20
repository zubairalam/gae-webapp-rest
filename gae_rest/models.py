from google.appengine.ext import ndb as db
from gae_rest import serializers


class App(db):
    name = db.StringProperty()


class AppSerializer(serializers.Serializer):
    name = serializers.StringProperty()
    created_at = serializers.DateTimeProperty(auto_created=True)
    updated_at = serializers.DateTimeProperty(auto_update=True)

app_serializer = AppSerializer(data={'name': 'com.tencent.ig'})

app_serializer.is_valid()

app_serializer.validated_data

app_serializer.save()

app_serializer.object # --> object of App model class