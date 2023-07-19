# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from airavata_mft_sdk.http import HttpCredential_pb2 as http_dot_HttpCredential__pb2


class HTTPSecretServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getHTTPSecret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.http.HTTPSecretService/getHTTPSecret',
                request_serializer=http_dot_HttpCredential__pb2.HTTPSecretGetRequest.SerializeToString,
                response_deserializer=http_dot_HttpCredential__pb2.HTTPSecret.FromString,
                )
        self.createHTTPSecret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.http.HTTPSecretService/createHTTPSecret',
                request_serializer=http_dot_HttpCredential__pb2.HTTPSecretCreateRequest.SerializeToString,
                response_deserializer=http_dot_HttpCredential__pb2.HTTPSecret.FromString,
                )
        self.updateHTTPSecret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.http.HTTPSecretService/updateHTTPSecret',
                request_serializer=http_dot_HttpCredential__pb2.HTTPSecretUpdateRequest.SerializeToString,
                response_deserializer=http_dot_HttpCredential__pb2.HTTPSecretUpdateResponse.FromString,
                )
        self.deleteHTTPSecret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.http.HTTPSecretService/deleteHTTPSecret',
                request_serializer=http_dot_HttpCredential__pb2.HTTPSecretDeleteRequest.SerializeToString,
                response_deserializer=http_dot_HttpCredential__pb2.HTTPSecretDeleteResponse.FromString,
                )


class HTTPSecretServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getHTTPSecret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createHTTPSecret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateHTTPSecret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteHTTPSecret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HTTPSecretServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getHTTPSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.getHTTPSecret,
                    request_deserializer=http_dot_HttpCredential__pb2.HTTPSecretGetRequest.FromString,
                    response_serializer=http_dot_HttpCredential__pb2.HTTPSecret.SerializeToString,
            ),
            'createHTTPSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.createHTTPSecret,
                    request_deserializer=http_dot_HttpCredential__pb2.HTTPSecretCreateRequest.FromString,
                    response_serializer=http_dot_HttpCredential__pb2.HTTPSecret.SerializeToString,
            ),
            'updateHTTPSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.updateHTTPSecret,
                    request_deserializer=http_dot_HttpCredential__pb2.HTTPSecretUpdateRequest.FromString,
                    response_serializer=http_dot_HttpCredential__pb2.HTTPSecretUpdateResponse.SerializeToString,
            ),
            'deleteHTTPSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteHTTPSecret,
                    request_deserializer=http_dot_HttpCredential__pb2.HTTPSecretDeleteRequest.FromString,
                    response_serializer=http_dot_HttpCredential__pb2.HTTPSecretDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.airavata.mft.credential.service.http.HTTPSecretService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HTTPSecretService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getHTTPSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.http.HTTPSecretService/getHTTPSecret',
            http_dot_HttpCredential__pb2.HTTPSecretGetRequest.SerializeToString,
            http_dot_HttpCredential__pb2.HTTPSecret.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createHTTPSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.http.HTTPSecretService/createHTTPSecret',
            http_dot_HttpCredential__pb2.HTTPSecretCreateRequest.SerializeToString,
            http_dot_HttpCredential__pb2.HTTPSecret.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateHTTPSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.http.HTTPSecretService/updateHTTPSecret',
            http_dot_HttpCredential__pb2.HTTPSecretUpdateRequest.SerializeToString,
            http_dot_HttpCredential__pb2.HTTPSecretUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteHTTPSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.http.HTTPSecretService/deleteHTTPSecret',
            http_dot_HttpCredential__pb2.HTTPSecretDeleteRequest.SerializeToString,
            http_dot_HttpCredential__pb2.HTTPSecretDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
