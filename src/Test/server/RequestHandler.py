from os import posix_fadvise
from threading import Thread
import pickle
from socketserver import BaseRequestHandler
from ..Message import Message

MAX_LIMIT = 1024

class RequestHandler(BaseRequestHandler):
    def __handle_end_test(self):
        th = Thread(target = self.server.shutdown)
        th.start()

        send_data = Message('Test ended...')
        packed_data = pickle.dumps(send_data)
        self.request.sendall(packed_data)
        

    def __handle_get_rem_time():
        pass

    def handle(self) -> None:
        rec_data = self.request.recv(MAX_LIMIT)
        unpacked_data = pickle.loads(rec_data)
        print(unpacked_data.message)

        if unpacked_data.message == 'STOP':
            self.__handle_end_test()
        elif unpacked_data.message == 'GET-REM-TIME':
            self.__handle_get_rem_time()
        else:
            pass

        # Running in another thread to prevent deadlock
        
