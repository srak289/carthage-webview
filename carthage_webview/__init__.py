from carthage.dependency_injection import inject, Injector, AsyncInjector

from . import server

@inject(injector=Injector)
def carthage_plugin(injector):
    injector.get_instance(AsyncInjector).loop.create_task(server.amain())
