from chilo_api import Chilo


api = Chilo(
    api_type='grpc',
    handlers='api/handlers',
    protobufs='api/protobufs',
    reflection=True,
    port=50051
)
