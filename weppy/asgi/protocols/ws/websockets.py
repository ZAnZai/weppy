# -*- coding: utf-8 -*-
"""
    weppy.asgi.protocols.ws.websockets
    ----------------------------------

    :copyright: (c) 2014-2019 by Giovanni Barillari
    :license: BSD, see LICENSE for more details.
"""

from . import ProtocolWrapper, protocols


@protocols.register('websockets', packages=['websockets'])
class WebsocketsProtocol(ProtocolWrapper):
    @classmethod
    def protocol_cls(cls):
        from uvicorn.protocols.ws.websockets_impl import WebSocketProtocol
        return WebSocketProtocol