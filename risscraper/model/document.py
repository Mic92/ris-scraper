# encoding: utf-8

"""
Copyright (c) 2012 Marian Steinbach

Hiermit wird unentgeltlich jeder Person, die eine Kopie der Software und
der zugehörigen Dokumentationen (die "Software") erhält, die Erlaubnis
erteilt, sie uneingeschränkt zu benutzen, inklusive und ohne Ausnahme, dem
Recht, sie zu verwenden, kopieren, ändern, fusionieren, verlegen
verbreiten, unterlizenzieren und/oder zu verkaufen, und Personen, die diese
Software erhalten, diese Rechte zu geben, unter den folgenden Bedingungen:

Der obige Urheberrechtsvermerk und dieser Erlaubnisvermerk sind in allen
Kopien oder Teilkopien der Software beizulegen.

Die Software wird ohne jede ausdrückliche oder implizierte Garantie
bereitgestellt, einschließlich der Garantie zur Benutzung für den
vorgesehenen oder einen bestimmten Zweck sowie jeglicher Rechtsverletzung,
jedoch nicht darauf beschränkt. In keinem Fall sind die Autoren oder
Copyrightinhaber für jeglichen Schaden oder sonstige Ansprüche haftbar zu
machen, ob infolge der Erfüllung eines Vertrages, eines Delikts oder anders
im Zusammenhang mit der Software oder sonstiger Verwendung der Software
entstanden.
"""

from base import Base
import hashlib


class Document(Base):
  """
  An document class
  """
  def __init__(self, identifier=None, numeric_id=None, title=None, size=None,
      mime_type=None, date=None, last_modified=None, sha1_checksum=None, original_url=None,
      slug=None, content=None):
    self.identifier = identifier
    self.numeric_id = numeric_id
    self.title = title
    self.x_content = content
    self.mime_type = mime_type
    self.date = date
    self.last_modified = last_modified
    self.sha1_checksum = sha1_checksum
    self.size = size
    self.slug = slug
    self.original_url = original_url
    super(Document, self).__init__()

  @property
  def content(self):
    return self.x_content

  @content.setter
  def content(self, value):
    self.x_content = value
    if value is None:
      self.size = None
      self.sha1_checksum = None
    else:
      self.size = len(value)
      self.sha1_checksum = hashlib.sha1(value).hexdigest()
