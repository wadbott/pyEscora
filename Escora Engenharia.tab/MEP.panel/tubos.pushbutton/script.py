# -*- coding: utf-8 -*-
"""Procura e muda a cor de todos os tubos com mais de 6 metros"""
__title__ = 'Verificador\nTubos'
__author__ = 'Wadham Bottacin'

import os
import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Plumbing import *
from pyrevit import forms
import math

 
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application
doc_title = __revit__.ActiveUIDocument.Document.Title

class units:
	@staticmethod
	def ft_to_mm(value):		
		return value * 0.3048


class TuboForm(forms.WPFWindow):
	def __init__(self, xaml_file_name):
		forms.WPFWindow.__init__(self, xaml_file_name)
		self.InfoBox.Text = "Clique em Buscar para pintar de vermelho os tubos com mais de 6 metros"

		collector = FilteredElementCollector(doc)
		self.pipes = collector.OfCategory(BuiltInCategory.OST_PipeCurves).WhereElementIsNotElementType().ToElements()
		collector = FilteredElementCollector(doc)
		self.pipe_fittings = collector.OfCategory(BuiltInCategory.OST_PipeFitting).WhereElementIsNotElementType().ToElements()
		collector = FilteredElementCollector(doc)
		self.plumb_fix = collector.OfCategory(BuiltInCategory.OST_PlumbingFixtures).WhereElementIsNotElementType().ToElements()
			
	
	def CloseButton(self, sender, e):
		self.Close()

	def SearchButton(self, sender, e):
		ExecuteSearch(self, self.pipes, self.pipe_fittings, self.plumb_fix)


def ExecuteSearch(self, p, pf, pfix):
	tubos_6m = []
	self.ProgressBar.Value = 0
	self.ProgressBar.Maximum = len(p) + len(pf) + len(pfix)	

	t = Transaction(doc, "TUBOS DE 6m")
	t.Start()	
	for pipe in p:
		length = pipe.Location.Curve.Length
		pipe_id = pipe.Id.IntegerValue

		if length >= 6:
			#print(pipe.Location.Curve.Length)
			tubos_6m.append(pipe)			

			color = Color(255,50,50)			

			ogs = OverrideGraphicSettings()\
					.SetProjectionLineColor(color)		

			doc.ActiveView.SetElementOverrides(ElementId(pipe_id), ogs)

		else:
			color = Color(0,0,0)
			ogs = OverrideGraphicSettings()\
					.SetProjectionLineColor(color)
			doc.ActiveView.SetElementOverrides(ElementId(pipe_id), ogs)

		self.ProgressBar.Value += 1

	for pipe_fitting in pf:
		
		pipe_fitting_id = pipe_fitting.Id.IntegerValue

		color = Color(0,0,0)

		ogs = OverrideGraphicSettings()\
				.SetProjectionLineColor(color)
		doc.ActiveView.SetElementOverrides(ElementId(pipe_fitting_id), ogs)

		self.ProgressBar.Value += 1	

	for plumb_fix in pfix:
		
		plumb_fix_id = plumb_fix.Id.IntegerValue

		color = Color(0,0,0)

		ogs = OverrideGraphicSettings()\
				.SetProjectionLineColor(color)
		doc.ActiveView.SetElementOverrides(ElementId(plumb_fix_id), ogs)

		self.ProgressBar.Value += 1	


	t.Commit()

		

	self.InfoBox.Text = "PROJETO: " + doc_title +"\n\nExistem "+\
						str(len(pf)) + " conexões." +\
						"\n\nExistem " + str(len(p)) +" tubos no projeto.\n " +\
						"Desses, " + str(len(tubos_6m)) +" tubos tem mais de 6 metros. \n\n"
	





if __name__ == '__main__':
	TuboForm("ui.xaml").show(modal=True)



