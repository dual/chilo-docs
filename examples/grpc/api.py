from chilo_api import Chilo


api = Chilo(
    api_type='grpc',
    handlers='handlers',
    protobufs='protobufs',
    reflection=True,
    port=50051
)
