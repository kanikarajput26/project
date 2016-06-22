from django.core.management.base import BaseCommand, CommandError
import boxer.utils as utils


class Command(BaseCommand):
    help = "it saves indiatimes news."

    def handle(self,*args,**options):
        g1 = utils.wegGetter("http://www.indiatimes.com/feeds/feeds.json")
        items = utils.processor(g1)
        for item in items:
            utils.saver(item)
        return


