from core import Core

class event_handler(Core):
    
    @staticmethod
    def put(session, target, path, **options):
        return True

    @staticmethod
    def sync(session, target, path, **options):
        return True

    @staticmethod
    def append(session, target, path, **options):
        return True

