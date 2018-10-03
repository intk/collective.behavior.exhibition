from Products.CMFCore.utils import getToolByName
from collective.behavior.exhibition.interfaces import IExhibition
from plone.directives import form
from zope.interface import alsoProvides
from zope.interface import implements
from zope.lifecycleevent import modified


alsoProvides(IExhibition, form.IFormFieldProvider)


class Exhibition(object):
    """
    """
    implements(IExhibition)

    def __init__(self, context):
        self.context = context
