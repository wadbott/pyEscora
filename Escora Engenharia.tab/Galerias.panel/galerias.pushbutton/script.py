# -*- coding: utf-8 -*-
__title__ = 'Criar\nGaleria'
__author__ = 'Wadham Bottacin'

import os
from pyrevit import forms
import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
import math
 
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application

class Galeria:
	def create_04(self,w,h,t1,b1,e1,d1,l):
		self.w = w
		self.h = h
		self.t1 = t1
		self.b1 = b1
		self.e1 = e1
		self.d1 = d1
		self.l = l

		#Family symbol name to place.
		symbName = 'SOFiSTiK_1_T-Beam_double_slope'
		refName = 'SOFiSTiK_Reference_Point'
		 
		#create a filtered element collector set to Category OST_Mass and Class FamilySymbol 
		collector = FilteredElementCollector(doc)
		collector.OfCategory(BuiltInCategory.OST_GenericModel)
		collector.OfClass(FamilySymbol)
		 
		famtypeitr = collector.GetElementIdIterator()
		famtypeitr.Reset()

		refptarr = ReferencePointArray()
		refptarr_axis = ReferencePointArray()

		for i in range(0,20):		         
			x = i*20
			y = 0           
			z = 0
         
			myXYZ = XYZ(x,y,z)
			refPt = doc.FamilyCreate.NewReferencePoint(myXYZ)
			refPt.CoordinatePlaneVisibility = CoordinatePlaneVisibility.Always
			refPt.ShowNormalReferencePlaneOnly = False
			refptarr.Append(refPt)	

		crv = doc.FamilyCreate.NewCurveByPoints(refptarr)		


		for item in famtypeitr:
			famtypeID = item
			famsymb = doc.GetElement(famtypeID)
	        #If the FamilySymbol is the name we are looking for, create a new instance.  
			if famsymb.Family.Name == symbName: 
		        #use for loop to create a series of points
				for i in range(0,20): 
					x = i*20
					y = 0           
					z = 0
		         
					myXYZ = XYZ(x,y,z)

					adaptComp = AdaptiveComponentInstanceUtils.CreateAdaptiveComponentInstance(doc, famsymb)
					adptPoints = AdaptiveComponentInstanceUtils.GetInstancePlacementPointElementRefIds(adaptComp)

		     
		            #Starting adaptive point locations.  get_Element returns a Reference Point
					aPt1 = doc.GetElement(adptPoints[0])		   	     	      
		     
		            #Desired Adaptive Point Locations
					loc1 = myXYZ		      
		     
		            #Some vector math to get the translation for MoveElement()
					trans1 = loc1.Subtract(aPt1.Position)				     
		     
					transform = Transform.CreateTranslation(trans1)				
					#AdaptiveComponentInstanceUtils.MoveAdaptiveComponentInstance(adaptComp, transform, False)

					myLine = Line.CreateBound(XYZ(0,0,0) , XYZ(100,0,0))						
		 			
			
					location = PointLocationOnCurve(PointOnCurveMeasurementType.SegmentLength, i*20, PointOnCurveMeasureFrom.Beginning)								
					pointOnEdge = doc.Application.Create.NewPointOnEdge(crv.GeometryCurve.Reference, location)					
					
					
					aPt1.SetPointElementReference(pointOnEdge)


class CustomISelectionFilter(ISelectionFilter):
    def __init__(self, category_name):
        self.category_name = category_name

    def AllowElement(self, e):
        if e.Category.Name == self.category_name:
            return True
        else:
            return False
    def AllowReference(self, ref, point):
        return true



class GaleriaForm(forms.WPFWindow):
	def __init__(self, xaml_file_name):
		forms.WPFWindow.__init__(self, xaml_file_name)	

		#Pick the line that will be the axis
		pick = uidoc.Selection.PickObject(ObjectType.Element, CustomISelectionFilter("Linhas"))
		line = doc.GetElement(pick.ElementId).GeometryCurve
		print(line.Direction)
		print(line.Length)
		print(line.Origin)
		print(line.GetEndPoint(0))
		print(line.GetEndPoint(1))		

		#Profile Family that will be opened  
  		file_dir = os.path.dirname(__file__)
  		path = str(os.path.join(file_dir, 'FAMILY', 'Galeria_simples.rfa')) 
		new_profile = app.OpenDocumentFile( path )

		#Search for ThreeDimensional view and store the element
		collector = FilteredElementCollector(new_profile)
		viewTypeColl = collector.OfClass(ViewFamilyType)
		for i in viewTypeColl:
			if i.ViewFamily == ViewFamily.ThreeDimensional:
				viewType = i
			else:
				continue

		#Going to create View3D in the document new_profile and place inside preview grid
		t = Transaction(new_profile, 'Criar 3D para o preview') 
		t.Start()
		NEW_view = View3D.CreateIsometric(new_profile, viewType.Id)
		preview = PreviewControl( new_profile, new_profile.GetElement(NEW_view.Id).Id )
		self.profile_preview.Children.Add(preview)
		t.Commit()

	



	def cancelar_button(self,sender,e):
		self.Close()			
	

	#def galeria_criar(self,sender,e):
		
		#start_creation(self)


def start_creation(self):
	t = Transaction(doc, 'Criar Galeria')
 
	t.Start()

	g = Galeria()
	g.create_04(self.w,self.h,self.t1,self.b1,self.e1,self.d1,self.l)

	t.Commit()
 
	#__window__.Close()
 
	
if __name__ == '__main__':
	GaleriaForm("ui.xaml").show(modal=True)



