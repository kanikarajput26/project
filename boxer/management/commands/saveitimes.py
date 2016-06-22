from django.core.management.base import BaseCommand, CommandError
import boxer.utils2 as utils2


class Command(BaseCommand):
    help = "it saves itimes news."

    def handle(self,*args,**options):
        g1 = utils2.wegGetter("http://api.itimes.com/thirdparty/rssfeeds/all")
        items = utils2.processor(g1)
        for item in items:
            utils2.saver(item)
        return
