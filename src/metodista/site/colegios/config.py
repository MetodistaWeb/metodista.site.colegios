# -*- coding:utf-8 -*-
from five import grok
from Products.CMFQuickInstallerTool import interfaces as qi_interfaces
from Products.CMFPlone import interfaces as st_interfaces

PROJECTNAME = 'metodista.site.colegios'

DEPS = [
    'Products.PloneFormGen',
    'collective.cover',
    'collective.polls',
    'plone.app.theming',
    'plone.app.contenttypes',
]

HIDDEN_PROFILES = [
    'collective.cover:default',
    'collective.cover:testfixture',
    'collective.cover:uninstall',
    'collective.polls:default',
    'plone.app.blocks:default',
    'plone.app.dexterity:default',
    'plone.app.drafts:default',
    'plone.app.iterate:plone.app.iterate',
    'plone.app.openid:default',
    'plone.app.relationfield:default',
    'plone.app.tiles:default',
    'plone.formwidget.autocomplete:default',
    'plone.formwidget.contenttree:default',
    'Products.PloneFormGen:default',
]


class HiddenProducts(grok.GlobalUtility):

    grok.implements(qi_interfaces.INonInstallable)
    grok.provides(qi_interfaces.INonInstallable)
    grok.name(PROJECTNAME)

    def getNonInstallableProducts(self):
        products = []
        products = [p for p in DEPS]
        return products


class HiddenProfiles(grok.GlobalUtility):

    grok.implements(st_interfaces.INonInstallable)
    grok.provides(st_interfaces.INonInstallable)
    grok.name(PROJECTNAME)

    def getNonInstallableProfiles(self):
        return HIDDEN_PROFILES
