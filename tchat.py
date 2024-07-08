"""Terminal Chat.
"""

import asyncio
import netifaces
import sys


class TServer:
    """TChat Server class.
    """

    def __init__(self, addr='', port):
        """Initialize self. See help(type(self)) for accurate signature.

        Args:
            addr (str): the address to listen on.
            port (port): the port number.
        """

        self.addr = addr
        self.port = port

    async def recv(reader):
        """Get response/message from a client.

        Args:
            reader (StreamReader): stream object to read data from.

        Return:
            return the received data in decoded form on success.
            return None on failure.
        """

        if reader:
            data = await reader.read(1024)

            return data.decode()

        return None

    async def handle_requests(self, reader, writer):
        """Asynchronous function to handle client connections.

        Args:
            reader (StreamReader): stream object to receive requests.
            writer (StreamWriter): stream object to send responses.

        Return:
            return nothing.
        """

        try:
            while True:
                request = await self.recv(reader)
                if request:
                    recvd = json.loads(request)     # requests are in json data

                    proto = recvd.get('proto')

                head = {
                    'proto': proto,
                    'status': [status_c, status_s],
                    'server': self.addr,
                    'datetime': [date, time, timezone],
                    'content': [content_t, content_l],
                    'last-modified': [date, time, timezone],
                    'etag': etag,
                    'accept-ranges': [ranges],
                }

                body = 'Connection Successfull'
                req = recv.get('req')
                if req == 'HEAD':
                    resp = await send(writer, json.dumps(head))

                resp = await send(writer, body)

        except (BrokenPipeError, ConnectionResetError):
            writer.close()

        except KeyboardInterrupt:
            writer.close()
            await writer.wait_closed()

            sys.exit()

    async def start(self):
        """Starts the asynchronous server.
        """

        server = await asyncio.start_server(self.handle_request, self.addr,
                                            self.port, family=netifaces.AF_INET
                                           )

    def run():
        """Runs the tchat server
        """

    try:
        asyncio.run(self.start())
    except KeyboardInterrupt:
        sys.exit()


class TClient:
    """TChat Client class.
    """

    def __init__(self, host):
        """Initialize self. See help(type(self)) for accurate signature.

        Args:
            host (str): the host to connect to (<addr>:<port>)
        """

        self.host = host

    def run_client():
        """Run the tchat client.
        """
