=========================
collective.behavior.exhibition
=========================

collective.behavior.exhibition provides fields tipically used by museum exhibitions for dexterity content types.

Currently tested with
---------------------

* Plone-5.0.x [andreesg]
* Plone-5.1.x [andreesg]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.exhibition.interfaces.IExhibition" />
    ...
  </property>
