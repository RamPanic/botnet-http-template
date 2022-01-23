
from schemas.schema import marshmallow

class CommandSchema(marshmallow.Schema):

    class Meta:

        fields = ("line", "output",)

cmd_schema = CommandSchema()
cmds_schema = CommandSchema(many=True)