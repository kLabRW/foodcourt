from rapidsms.apps.base import AppBase

class EchoApp(AppBase):

  def handle(self, request):
      request.respond("You sent: %s" % request.text)
      return True
