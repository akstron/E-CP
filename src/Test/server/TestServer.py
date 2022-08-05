from socketserver import TCPServer

class TestServer(TCPServer):
    def __init__(self, server_address: tuple[str, int], RequestHandlerClass) -> None:
        super().__init__(server_address, RequestHandlerClass)

    def start_test_server(self):
        print('Starting...')
        super().serve_forever()

    def stop_test_server(self):
        print('Stopping...')
        super().shutdown()