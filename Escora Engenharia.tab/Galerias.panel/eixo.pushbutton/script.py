#-*- coding: utf-8 -*-
__title__ = 'Criar\nEixo'
__author__ = 'Wadham Bottacin'

import os
from pyrevit import forms
from pyrevit import coreutils
import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import PreviewControl
import math
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application


class AxisData:
	horizontal = []
	vertical = []

	#Convert DECIMAL_FEET to revit's internal units
	@staticmethod	
	def c(value):
		converted_value = UnitUtils.ConvertToInternalUnits(value, DisplayUnitType.DUT_DECIMAL_FEET)
		return converted_value

	class HorizontalData(object):
		def __init__(self, TYPE, LENGH, RI, RF, H_STATION):
			self.TYPE = TYPE
			self.LENGH = LENGH
			self.RI = RI
			self.RF = RF
			self.H_STATION = H_STATION

		@staticmethod
		def GetHorInitialData():			
			AxisData.horizontal.append(AxisData.HorizontalData("Linha",AxisData.c(100),"-","-",AxisData.c(100)))
			AxisData.horizontal.append(AxisData.HorizontalData("Arco",AxisData.c(60),AxisData.c(30),AxisData.c(30),AxisData.c(100)))

			return AxisData.horizontal

		@staticmethod
		def NewRow():
			row = AxisData.HorizontalData("","","","","")
			AxisData.horizontal.append(row)			

		@staticmethod
		def DeleteRow():
			AxisData.horizontal = AxisData.horizontal[:-1]			

	class VerticalData(object):
		def __init__(self, V_STATION, HEIGHT):
			self.V_STATION = V_STATION
			self.HEIGHT = HEIGHT
			self.vertical = []	
		
		@staticmethod
		def GetVerInitialData():			
			AxisData.vertical.append(AxisData.VerticalData(AxisData.c(0), AxisData.c(0)))

			return AxisData.vertical

		@staticmethod
		def NewRow():
			row = AxisData.VerticalData("","")
			AxisData.vertical.append(row)
			
		@staticmethod
		def DeleteRow():
			AxisData.vertical = AxisData.vertical[:-1]

class Axis:
	def __init__(self, horizontal, vertical, OriginX, OriginY, doc):
		self.horizontal = horizontal
		self.vertical = vertical
		self.OriginX = OriginX
		self.OriginY = OriginY
		self.doc = doc

		for obj in horizontal:
			self.TYPE = obj.TYPE
			if self.TYPE == "Linha":
				self.LENGH = obj.LENGH
				Axis.Line(self.LENGH, self.OriginX, self.OriginY, self.doc)				

			if self.TYPE == "Arco":
				self.LENGH = obj.LENGH
				self.RI = obj.RI
				self.RF = obj.RF

	@classmethod
	def Line(self, LENGH, OriginX, OriginY, doc):
		#Create a plane by normal and origin
		origin = XYZ(int(OriginX), int(OriginY), 0)
		normal = XYZ.BasisZ
		 
		plane = Plane.CreateByNormalAndOrigin(normal, origin)

		#Create a sketch plane
		skplane = SketchPlane.Create(doc ,plane)
		 
		#Create line vertices
		lnStart = origin
		lnEnd = XYZ(int(LENGH), 0, 0)
		 
		#create NewLine()
		line = Line.CreateBound(lnStart, lnEnd)
		 
		#create NewModelCurve()
		crv = doc.FamilyCreate.NewModelCurve(line, skplane)

	

	def Arc():
		print("arco")			

class EixoForm(forms.WPFWindow):
	def __init__(self, xaml_file_name):
		forms.WPFWindow.__init__(self, xaml_file_name)

		#Open a family template insite path
		file_dir = os.path.dirname(__file__)
  		path = str(os.path.join(file_dir, 'FAMILY', 'Metric_Generic_Model_Adaptive_Axis_Base.rft')) 
		self.new_profile = app.OpenDocumentFile( path )

		#Search for ThreeDimensional view and store the element
		collector = FilteredElementCollector(self.new_profile)
		viewTypeColl = collector.OfClass(ViewFamilyType)
		for i in viewTypeColl:
			if i.ViewFamily == ViewFamily.ThreeDimensional:
				viewType = i
			else:
				continue

		#Going to create View3D in the document new_profile and place inside preview grid
		t = Transaction(self.new_profile, 'Criar 3D para o preview') 
		t.Start()
		NEW_view = View3D.CreateIsometric(self.new_profile, viewType.Id)
		preview = PreviewControl(self.new_profile, self.new_profile.GetElement(NEW_view.Id).Id )
		self.MainGrid.Children.Add(preview)
		t.Commit()

		self.HorizontalGrid.ItemsSource = AxisData.HorizontalData.GetHorInitialData()	
		self.VerticalGrid.ItemsSource = AxisData.VerticalData.GetVerInitialData()
		self.OriginX.Text = "0"
		self.OriginY.Text = "0"


	def add_horizontal_row(self,sender,e):
		AxisData.HorizontalData.NewRow()
		self.HorizontalGrid.Items.Refresh()
		self.HorizontalGrid.ItemsSource = AxisData.horizontal

	def delete_horizontal_row(self,sender,e):
		AxisData.HorizontalData.DeleteRow()
		self.HorizontalGrid.Items.Refresh()
		self.HorizontalGrid.ItemsSource = AxisData.horizontal				

	def add_vertical_row(self,sender,e):
		AxisData.VerticalData.NewRow()
		self.VerticalGrid.Items.Refresh()
		self.VerticalGrid.ItemsSource = AxisData.vertical

	def delete_vertical_row(self,sender,e):
		AxisData.VerticalData.DeleteRow()
		self.VerticalGrid.Items.Refresh()
		self.VerticalGrid.ItemsSource = AxisData.vertical
	
	def ok_horizontal(self,sender,e):
		t = Transaction(self.new_profile, 'Create Line')
		 
		t.Start()

		a = Axis(AxisData.horizontal, AxisData.vertical, self.OriginX.Text, self.OriginY.Text, self.new_profile)
		
		 
		t.Commit()		

	def ok_vertical(self,sender,e):
		print("Deu certo")		
		
	def cancelar_button(self,sender,e):
		self.Close()


def start_creation(self):
	t = Transaction(doc, 'Criar Eixo')
 
	t.Start()

	g = Galeria()
	g.create_04(self.w,self.h,self.t1,self.b1,self.e1,self.d1,self.l)

			
 
	#__window__.Close()
 
	
if __name__ == '__main__':
	EixoForm("ui.xaml").show(modal=True)



