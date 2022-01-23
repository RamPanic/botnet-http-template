
from schemas.schema import marshmallow

class BotSchema(marshmallow.Schema):

    class Meta:

        fields = (

            "uuid", 
            "hostname", 
            "username", 
            "os", 
            "datetime", 
            "remote_ip", 
            "local_ip", 
            "state", 
            "location",
        
        )

bot_schema = BotSchema()
bots_schema = BotSchema(many=True)