from django.db import models

class pubs(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    sources = models.ManyToManyField('isro.source', related_name='+', blank = False)
    link = models.URLField(max_length=300, default='')

    def add_srcs(self, ss):
        # method to add multiple sources
        # ss should be a queryset
        for s in ss:
            self.add_src(s)

    def add_src(self, s):
        # method to add single source
        # both data-points should be saved in the database initially.
        self.sources.add(s)
        s.pubs.add(self)
        s.save()
        self.save()

    def __str__(self):
        return self.title

