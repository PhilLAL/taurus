#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
## 
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

__all__ = ["DropDebugger"]
__docformat__ = 'restructuredtext'

from taurus.qt import Qt

class DropDebugger(Qt.QLabel):
    '''A simple utility for debugging drag&drop. 
    This widget will accept drops and show a pop-up with the contents 
    of the MIME data passed in the drag&drop'''  

    def __init__(self, parent=None):
        Qt.QLabel.__init__(self, parent)
        self.setAcceptDrops(True)
        self.setText('Drop something here')
        self.setMinimumSize(300,200)
        self.setWindowTitle('Drag&Drop Debugger')
             
    def dragEnterEvent(self,event):
        event.acceptProposedAction() 
        
    def dropEvent(self, event):
        '''reimplemented to support drag&drop of models. See :class:`QWidget`'''
        msg = '<b>MIMETYPE</b>: DATA. <ul>'
        for format in mimedata.formats():
            data = mimedata.data(format)
            msg += '<li><b>%s</b>: "%s"</li>'% (format, unicode(data))
        msg+='</ul>'
        Qt.QMessageBox.information( self, "Drop event received", msg)
        

if __name__=='__main__':
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    w=DropDebugger()
    w.show()
    sys.exit(app.exec_())
