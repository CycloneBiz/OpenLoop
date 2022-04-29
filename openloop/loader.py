from openloop.alerts import AlertManager
from openloop.auth import Auth_Handler
from openloop.config import check as configCheck
from openloop.database import Database
from openloop.web import Web_Handler
from openloop.flow import Flow, Flow_Serve
from openloop.plugins import Deployer
from openloop.api import API_Handler

def load_data(app):
    """
    Applys blueprints and loads everything in one central class
    """
    class SharePoint:
        def __init__(self) -> None:
            self.app = app
            self.config = configCheck()
            self.database = Database(self)
            self.db = self.database.db
            self.auth = Auth_Handler(self)

            self.flow = Flow()
            self.alerts = AlertManager(self)

            app.register_blueprint(Flow_Serve(self.flow).web, url_prefix="/flow")

            self.plugins = Deployer()
            app.register_blueprint(API_Handler(self).api, url_prefix="/api")

            app.register_blueprint(Web_Handler(self).web)

    share = SharePoint()
    share.db.create_all()