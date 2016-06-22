from django.core.management.base import BaseCommand, CommandError
import boxer.utils4 as utils4


class Command(BaseCommand):
    help = "it saves naukarinama english news."

    def handle(self,*args,**options):
        g1 = utils4.wegGetter("https://www.naukrinama.com/feed/")
        item1 = utils4.processor1(g1)
        item2 = utils4.processor2(item1)
        item3 = utils4.processor3(item2)
        for i in range(0,len(item3)):
            item = item3[i]
            utils4.saver(item)
        return
