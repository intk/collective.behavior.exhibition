#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from plone.dexterity.interfaces import IDexterityContent
from plone.directives import form
from zope.interface import alsoProvides
from zope.interface import implements
from zope.lifecycleevent import modified
from five import grok
from zope.interface import implementer
from zope.component import adapter
from zope.interface import Interface
from zope.interface import provider
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import implementer
from zope.component import adapter
from plone.supermodel import model
from zope import schema
from collective.behavior.exhibition import _
from plone.directives import dexterity, form
from plone.indexer.decorator import indexer
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from collective import dexteritytextindexer
#
# DataGridFields dependencies
#
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow, IDataGridField
from collective.z3cform.datagridfield.blockdatagridfield import BlockDataGridFieldFactory



def find_century(year):
    if year > 1900:
        if year > 1830 and year <= 1840:
            return "1830-1840"
        elif year > 1840 and year <= 1850:
            return "1840-1850"
        elif year > 1850 and year <= 1860:
            return "1850-1860"
        elif year > 1860 and year <= 1870:
            return "1860-1870"
        elif year > 1870 and year <= 1880:
            return "1870-1880"
        elif year > 1880 and year <= 1890:
            return "1880-1890"
        elif year > 1890 and year <= 1900:
            return "1890-1900"
        elif year > 1900 and year <= 1910:
            return "1900-1910"
        elif year > 1910 and year <= 1920:
            return "1910-1920"
        elif year > 1920 and year <= 1930:
            return "1920-1930"
        elif year > 1930 and year <= 1940:
            return "1930-1940"
        elif year > 1940 and year <= 1950:
            return "1940-1950"
        elif year > 1950 and year <= 1960:
            return "1950-1960"
        elif year > 1960 and year <= 1970:
            return "1960-1970"
        elif year > 1970 and year <= 1980:
            return "1970-1980"
        elif year > 1980 and year <= 1990:
            return "1980-1990"
        elif year > 1990 and year <= 2000:
            return "1990-2000"
        elif year > 2000 and year <= 2010:
            return "2000-2010"
        elif year > 2010 and year <= 2020:
            return "2010-2020"
        else:
            if year < 0:
                return "Voor Christus"
            elif year <= 100:
                return "1e Eeuw"
            elif year % 100 == 0:
                return "%se Eeuw" %(str(year/100))
            else:
                return "%se Eeuw" %(str((year/100)+1))
    else:
        if year < 0:
            return "Voor Christus"
        elif year <= 100:
            return "1e Eeuw"
        elif year % 100 == 0:
            return "%se Eeuw" %(str(year/100))
        else:
            return "%se Eeuw" %(str((year/100)+1))

def safe_value(value):
    try:
        term = None
        if isinstance(value, unicode):
            # no need to use portal encoding for transitional encoding from
            # unicode to ascii. utf-8 should be fine.
            term = value.encode('utf-8')
            return term
        else:
            return value
    except:
        return None

class IListField(Interface):
    pass
 

class ListField(schema.List):
    grok.implements(IListField)
    pass

class IDocumentation(Interface):
    title = schema.TextLine(title=_(u'Title'), required=False, missing_value=u'', default=u'')
    lead_word = schema.TextLine(title=_(u'Lead word'), required=False, missing_value=u'', default=u'')
    year_of_publication = schema.TextLine(title=_(u'Year of publication'), required=False, missing_value=u'', default=u'')
    place_of_publication = schema.TextLine(title=_(u'Place of publication'), required=False, missing_value=u'', default=u'')
    pagination = schema.TextLine(title=_(u'pagination'), required=False, missing_value=u'', default=u'')
    statement_of_responsibility = schema.TextLine(title=_(u'Statement of responsability'), required=False, missing_value=u'', default=u'')
    
    authors = schema.List(title=_(u'Author'), required=False, default=[], missing_value=[], value_type=schema.TextLine())
    publishers = schema.List(title=_(u'Publisher'), required=False, default=[], missing_value=[], value_type=schema.TextLine())

    directives.widget(
        'authors',
        AjaxSelectFieldWidget,
        vocabulary='collective.object.author'
    )

    directives.widget(
        'publishers',
        AjaxSelectFieldWidget,
        vocabulary='collective.object.author'
    )

    author = schema.TextLine(title=_(u'Author'), required=False, missing_value=u'', default=u'')
    publisher = schema.TextLine(title=_(u'Pubisher'), required=False, missing_value=u'', default=u'')

@provider(IFormFieldProvider)
class IExhibition(model.Schema):
    """Interface for Exhibition behavior."""

    # exhibition fieldset
    model.fieldset(
        'exhibition',
        label=_(u'Exhibition', default=u'Exhibition'),
        fields=['priref', 'cm_nummer', 'alternative_title', 'start_date', 'end_date', 'organiser', 'designer', 'documentation', 'notes', 'show_notes', 'persistent_url'],
    )

    priref = schema.TextLine(
        title=_(u'priref', default=u'priref'),
        required=False
    )

    cm_nummer = schema.TextLine(
        title=_(u'cm_nummer', default=u'cm_nummer'),
        required=False
    )
    dexteritytextindexer.searchable('cm_nummer')

    alternative_title = schema.TextLine(
        title=_(u'alternative_title', default=u'Alternative title'),
        required=False
    )
    dexteritytextindexer.searchable('alternative_title')

    start_date = schema.TextLine(
        title=_(u'start_date', default=u'Start date'),
        required=False
    )
    dexteritytextindexer.searchable('start_date')

    end_date = schema.TextLine(
        title=_(u'end_date', default=u'End date'),
        required=False
    )
    dexteritytextindexer.searchable('end_date')

    organiser = schema.TextLine(
        title=_(u'organisation', default=u'Organisation'),
        required=False
    )
    dexteritytextindexer.searchable('organiser')

    designer = schema.TextLine(
        title=_(u'designer', default=u'Designer'),
        required=False
    )
    dexteritytextindexer.searchable('designer')

    documentation = ListField(title=_(u'documentation'),
        value_type=DictRow(title=_(u'documentation'), schema=IDocumentation),
        required=False)
    form.widget(documentation=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('documentation')

    notes = RichTextField(
        title=_(u'Notes'),
        description=u'',
        required=False,
    )
    form.widget('notes', RichTextFieldWidget)
    dexteritytextindexer.searchable('notes')

    show_notes = schema.Bool(
        title=_(
            u'show_notes',
            default=u'Show notes'
        ),
        description=_(
            u'show_notes_description',
            default=u'Activate to show the notes field'
        ),
        required=False,
        default=False
    )

    persistent_url = schema.TextLine(
        title=_(u'persistent_url', default=u'Persistent url'),
        required=False
    )
    dexteritytextindexer.searchable('persistent_url')


@indexer(IExhibition)
def exhibition_priref(object, **kw):
    try:
        if getattr(object, 'portal_type', None) == "Event":
            if hasattr(object, 'priref'):
                value = object.priref
                if value:
                    return value.lower()
                else:
                    return ""
            else:
                return ""
        else:
            return ""
    except:
        return ""

@indexer(IExhibition)
def is_exhibition(object, **kw):
    try:
        if getattr(object, 'portal_type', None) == "Event":
            if getattr(object, 'priref', ''):
                return True
            else:
                return False
        else:
            return False
    except:
        return False


@indexer(IExhibition)
def object_period_index(object, **kw):
    try:
        if getattr(object, 'portal_type', None) == "Event":
            if hasattr(object, 'start_date'):
                terms = []
                date_start = object.start_date
                date_start_split = date_start.split('-')
                if len(date_start_split) == 3:
                    date_year = int(date_start_split[0])
                    century = find_century(date_year)
                    terms.append(safe_value(century))
                    return terms
                else:
                    return []
            else:
                return []
        else:
            return []
    except:
        return []


        





