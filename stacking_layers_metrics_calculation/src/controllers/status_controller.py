from controllers.master_controller import MasterController
from libs.global_objects import GlobalObjects



class StatusController(MasterController):

    @staticmethod
    @MasterController.web_server.get("/status", description="Machine input status", name="App Status")
    def status():
        """
            show if service is receiving machine data
        """
        return {'Info': GlobalObjects.machine_input_messages_health}
