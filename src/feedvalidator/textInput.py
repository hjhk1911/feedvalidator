"""$Id$"""

__author__ = "Sam Ruby <http://intertwingly.net/> and Mark Pilgrim <http://diveintomark.org/>"
__version__ = "$Revision$"
__date__ = "$Date$"
__copyright__ = "Copyright (c) 2002 Sam Ruby and Mark Pilgrim"
__license__ = "Python"

from validators import *
from extension import extension

#
# textInput element.
#
class textInput(validatorBase, extension):
  def getExpectedAttrNames(self):
      return [(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#', u'about')]

  def validate(self):
    if not "title" in self.children:
      self.log(MissingTitle({"parent":self.name, "element":"title"}))
    if not "link" in self.children:
      self.log(MissingLink({"parent":self.name, "element":"link"}))
    if not "description" in self.children:
      self.log(MissingDescription({"parent":self.name,"element":"description"}))
    if not "name" in self.children:
      self.log(MissingElement({"parent":self.name, "element":"name"}))

  def do_title(self):
    return nonhtml(), noduplicates()

  def do_description(self):
    return text(), noduplicates()

  def do_name(self):
    return formname(), noduplicates()

  def do_link(self):
    return rfc2396_full(), noduplicates()

  def do_dc_creator(self):
    return text() # duplicates allowed

  def do_dc_subject(self):
    return text() # duplicates allowed

  def do_dc_date(self):
    return w3cdtf(), noduplicates()


__history__ = """
$Log$
Revision 1.6  2006/02/10 18:16:43  rubys
TextInput name check

Revision 1.5  2005/07/04 22:54:31  philor
Support rest of dc, dcterms, geo, geourl, icbm, and refactor out common extension elements

Revision 1.4  2005/07/02 19:26:44  rubys
Issue warnings for itunes tags which appear to contain HTML.

Note: this will also cause warnings to appear for titles and a
few other select tags (not descriptions!).  Previously, only
informational messages (which, by default, are not displayed)
were generated.

If this is a problem, we can change some individual tags, or
split this into two messages (one a warning, one informational).

Revision 1.3  2004/03/11 19:26:05  rubys
Allow rdf:about on textinput elements

Revision 1.2  2004/02/17 23:17:45  rubys
Commit fixes for bugs 889545 and 893741: requiring non-relative URLs in
places where a relative URL is OK (example: rdf).

Revision 1.1.1.1  2004/02/03 17:33:16  rubys
Initial import.

Revision 1.6  2003/12/11 16:32:08  f8dy
fixed id tags in header

Revision 1.5  2002/10/24 14:47:33  f8dy
decoupled "no duplicates" check from individual validator classes,
allow handlers to return multiple validator classes

Revision 1.4  2002/10/22 17:29:52  f8dy
loosened restrictions on link/docs/url protocols; RSS now allows any
IANA protocol, not just http:// and ftp://

Revision 1.3  2002/10/18 13:06:57  f8dy
added licensing information

"""
