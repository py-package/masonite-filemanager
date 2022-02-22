from masonite.foundation import Application, Kernel
from tests.integrations.config.providers import PROVIDERS
from tests.integrations.Kernel import Kernel as ApplicationKernel


"""Start The Application Instance."""
application = Application("tests/integrations")

"""Now Bind important providers needed to make the framework work."""
application.register_providers(Kernel, ApplicationKernel)

"""Now Bind important application specific providers needed to make the application work."""
application.add_providers(*PROVIDERS)
