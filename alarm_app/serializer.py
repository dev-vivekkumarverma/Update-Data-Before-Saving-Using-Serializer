from rest_framework import serializers
from .models import Alarm

    
class AlarmSerializer(serializers.ModelSerializer):
    # use when you want to modify data while retrival
    # def to_representation(self, value):
    #     return "rgb(%d, %d, %d)" % (value.red, value.green, value.blue)

    # use when you want to modify data while saving
    def to_internal_value(self, data):
        print("data:",data)
        # data =  super().to_internal_value(data)
        # print("data2:",data)
        # data["days"] = "+".join(data["days"].split(','))
        data["days"] = "+".join(data["days"])
        return data
    class Meta:
            model=Alarm
            fields="__all__"
    