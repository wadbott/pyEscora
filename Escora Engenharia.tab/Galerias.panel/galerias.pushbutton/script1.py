# -*- coding: utf-8 -*-
__title__ = 'Criar\nGaleria'
__author__ = 'Wadham Bottacin'

import os
from pyrevit import forms
import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import *
import math
 
doc = __revit__.ActiveUIDocument.Document
app = __revit__.Application

class Galeria:
	def create_06(self,w,h,t1,b1,e1,d1,l):
		self.w = w
		self.h = h
		self.t1 = t1
		self.b1 = b1
		self.e1 = e1
		self.d1 = d1
		self.l = l

		#define the profile for the extrusion

		curveArrArray = CurveArrArray()
		curveArray1 = CurveArray()
		curveArray2 = CurveArray()
		curveArray3 = CurveArray()

		#create a rectangular profile
		p0 = XYZ.Zero
		p1 = XYZ(100, 0, 0)
		p2 = XYZ(100, 100, 0)
		p3 = XYZ(0, 100, 0);

		p4 = XYZ(0, 0, 50)
		p5 = XYZ(200, 0, 50)
		p6 = XYZ(200, 200, 50)
		p7 = XYZ(0, 200, 50);

		line1 = Line.CreateBound(p0, p1)
		line2 = Line.CreateBound(p1, p2)
		line3 = Line.CreateBound(p2, p3)
		line4 = Line.CreateBound(p3, p0)

		line5 = Line.CreateBound(p4, p5)
		line6 = Line.CreateBound(p5, p6)
		line7 = Line.CreateBound(p6, p7)
		line8 = Line.CreateBound(p7, p4)

		curveArray1.Append(line1)
		curveArray1.Append(line2)
		curveArray1.Append(line3)
		curveArray1.Append(line4)

		curveArray2.Append(line1)
		curveArray2.Append(line2)
		curveArray2.Append(line3)
		curveArray2.Append(line4)

		curveArrArray.Append(curveArray1)
		curveArrArray.Append(curveArray2)

		origin = XYZ.Zero
		normal = XYZ.BasisZ		 
		plane = Plane.CreateByNormalAndOrigin(normal, origin)
		skplane = SketchPlane.Create(doc, plane)

		#create solid rectangular extrusion
		rectExtrusion = doc.FamilyCreate.NewExtrusion(True, curveArrArray, skplane, 300)

	def create_05(self,w,h,t1,b1,e1,d1,l):
		self.w = w
		self.h = h
		self.t1 = t1
		self.b1 = b1
		self.e1 = e1
		self.d1 = d1
		self.l = l


		#path = ReferenceArray()

		#path.Append(Line.CreateBound(XYZ.Zero, XYZ( 0, 50, 0 )))

		#use for loop to create a series of points
		for i in range(0,20):
		    x = i*20
		    y = i*20
		    #z is controlled using sine
		    z = math.sin(i)*50
		 
		    myXYZ = XYZ(x,y,z)
		    refPt = doc.FamilyCreate.NewReferencePoint(myXYZ)
		    refptarr.Append(refPt)
		 
		crv = doc.FamilyCreate.NewCurveByPoints(refptarr)

		#Create line vertices
		lnStart = XYZ(0,0,0)
		lnEnd = XYZ(0,700,0)
		 
		#create NewLine()
		line = Line.CreateBound(lnStart, lnEnd)
	

		curve1_arr = CurveArrArray()
		curve2_arr = CurveArrArray()
		
		curve1 = CurveArray()

		curve2 = CurveArray()

 
		#Create a plane by normal and origin
		origin = XYZ.Zero
		normal = XYZ.BasisZ
		 
		plane = Plane.CreateByNormalAndOrigin(normal, origin)

		#Create a sketch plane
		skplane = SketchPlane.Create(doc,plane) 
		 
		#Define arc parameters
		startAngle = 0
		endAngle = 2* math.pi
		radius = 100

		curve1.Append(Arc.Create(plane, radius, startAngle, endAngle))
		curve1_arr.Append(curve1)

		#Create a plane by normal and origin
		origin2 = XYZ(0,100,0)
		 
		plane2 = Plane.CreateByNormalAndOrigin(normal, origin2)

		#Create a sketch plane
		skplane2 = SketchPlane.Create(doc,plane2) 
		 
		#Define arc parameters
		startAngle = 0
		endAngle = 2* math.pi
		radius = 100

		crv = doc.FamilyCreate.NewModelCurve(line, skplane)		

		curve2.Append(Arc.Create(plane2, radius, startAngle, endAngle))
		curve2_arr.Append(curve2)

		profile1 = app.Create.NewCurveLoopsProfile(curve1_arr)
		profile2 = app.Create.NewCurveLoopsProfile(curve2_arr)

		swept = doc.FamilyCreate.NewSweptBlend(True, crv.GeometryCurve.Reference, profile1, profile2)



	def create_04(self,w,h,t1,b1,e1,d1,l):
		self.w = w
		self.h = h
		self.t1 = t1
		self.b1 = b1
		self.e1 = e1
		self.d1 = d1
		self.l = l

		#Family symbol name to place.
		symbName = 'Galeria_simples'
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
					ElementTransformUtils.RotateElement(doc, aPt1.Id, myLine, 0.5*math.pi)			
		 			
			
					location = PointLocationOnCurve(PointOnCurveMeasurementType.SegmentLength, i*20, PointOnCurveMeasureFrom.Beginning)								
					pointOnEdge = doc.Application.Create.NewPointOnEdge(crv.GeometryCurve.Reference, location)					
					
					
					aPt1.SetPointElementReference(pointOnEdge)
				

		


	def create_03(self,w,h,t1,b1,e1,d1,l):
		self.w = w
		self.h = h
		self.t1 = t1
		self.b1 = b1
		self.e1 = e1
		self.d1 = d1
		self.l = l
		pieces = int(self.l / 100)
		print(pieces)
		piece_l = 0
		h = 0

		#create Reference Array for curves		
		refptarr_axis = ReferencePointArray()
		RefArr_axis = ReferenceArray()
		RefArr_profiles = ReferenceArrayArray()	


		for i in range(0,pieces):
			print(i)		
			refpt_axis = doc.FamilyCreate.NewReferencePoint(XYZ(100,piece_l,75))

			refptarr_axis.Append(refpt_axis)	

			piece_l += 100

		axis_crv = doc.FamilyCreate.NewCurveByPoints(refptarr_axis)
		RefArr_axis.Append(axis_crv.GeometryCurve.Reference)


		for station in refptarr_axis:
			i = 0
			pts = []
			pts.append(station.Position)
			pts.append(XYZ(station.Position.X + self.w, station.Position.Y, station.Position.Z))
			pts.append(XYZ(station.Position.X + self.w, station.Position.Y, station.Position.Z + self.h))
			pts.append(XYZ(station.Position.X ,station.Position.Y, station.Position.Z + self.h))
			pts.append(station.Position)

			origin = station.Position		
			plane = Plane.CreateByThreePoints(origin, pts[1], pts[2])
			skplane = SketchPlane.Create(doc, plane)

			refptarr = ReferenceArray()		

			for i in range(0,len(pts)-1):
			    ptA = pts[i]
			    ptB = pts[i+1]

			    line = Line.CreateBound(ptA,ptB)
			    crv = doc.FamilyCreate.NewModelCurve(line,skplane)
			    refptarr.Append(crv.GeometryCurve.Reference)
			
			RefArr_profiles.Append(refptarr)

		

		sweptBlend = doc.FamilyCreate.NewSweptBlendForm(True, RefArr_axis, RefArr_profiles)


	def create_02(self,w,h,t1,b1,e1,d1,l):
		self.w = w
		self.h = h
		self.t1 = t1
		self.b1 = b1
		self.e1 = e1
		self.d1 = d1
		self.l = l		

        #Create a sketch plane
		origin = XYZ.Zero
		normal = XYZ.BasisY		 
		plane = Plane.CreateByNormalAndOrigin(normal, origin)
		skplane = SketchPlane.Create(doc, plane)
		 
		#Create line vertices extrusion
		lnPt1 = XYZ(0,0,0)
		lnPt2 = XYZ(self.w,0,0)
		lnPt3 = XYZ(self.w,0,self.h)
		lnPt4 = XYZ(0,0,self.h)

		#Create line vertices void
		void_lnPt1 = XYZ(self.e1, 0, self.b1)
		void_lnPt2 = XYZ(self.w - self.d1, 0, self.b1)
		void_lnPt3 = XYZ(self.w - self.d1, 0, self.h-self.t1)
		void_lnPt4 = XYZ(self.e1, 0, self.h - self.t1)
		 
		#create lines extrusion
		line1 = Line.CreateBound(lnPt1, lnPt2)
		line2 = Line.CreateBound(lnPt2, lnPt3)
		line3 = Line.CreateBound(lnPt3, lnPt4)
		line4 = Line.CreateBound(lnPt4, lnPt1)

		#create lines void
		void_line1 = Line.CreateBound(void_lnPt1, void_lnPt2)
		void_line2 = Line.CreateBound(void_lnPt2, void_lnPt3)
		void_line3 = Line.CreateBound(void_lnPt3, void_lnPt4)
		void_line4 = Line.CreateBound(void_lnPt4, void_lnPt1)
		 
		#create model curves from lines extrusion
		crvA = doc.FamilyCreate.NewModelCurve(line1, skplane)
		crvB = doc.FamilyCreate.NewModelCurve(line2, skplane)
		crvC = doc.FamilyCreate.NewModelCurve(line3, skplane)
		crvD = doc.FamilyCreate.NewModelCurve(line4, skplane)

		#create model curves from lines void
		void_crvA = doc.FamilyCreate.NewModelCurve(void_line1, skplane)
		void_crvB = doc.FamilyCreate.NewModelCurve(void_line2, skplane)
		void_crvC = doc.FamilyCreate.NewModelCurve(void_line3, skplane)
		void_crvD = doc.FamilyCreate.NewModelCurve(void_line4, skplane)
		 
		#create reference array and append with geometry curve references extrusion
		refarr = ReferenceArray()
		refarr.Append(crvA.GeometryCurve.Reference)
		refarr.Append(crvB.GeometryCurve.Reference)
		refarr.Append(crvC.GeometryCurve.Reference)
		refarr.Append(crvD.GeometryCurve.Reference)

		#create reference array and append with geometry curve references void
		void_refarr = ReferenceArray()
		void_refarr.Append(void_crvA.GeometryCurve.Reference)
		void_refarr.Append(void_crvB.GeometryCurve.Reference)
		void_refarr.Append(void_crvC.GeometryCurve.Reference)
		void_refarr.Append(void_crvD.GeometryCurve.Reference)

		#establish extrusion vector
		dir = XYZ(150,self.l,300)
		 
		#extrude the form
		extrude = doc.FamilyCreate.NewExtrusionForm(True,refarr,dir)

		#void the form
		void = doc.FamilyCreate.NewExtrusionForm(False,void_refarr,dir)

	def create_01(self,w,h,t1,b1,e1,d1,l):
		self.w = w
		self.h = h
		self.t1 = t1
		self.b1 = b1
		self.e1 = e1
		self.d1 = d1
		self.l = l
				
		 		 
		#Create line vertices profile 1
		lnPt1 = XYZ.Zero
		lnPt2 = XYZ(self.w,0,0)
		lnPt3 = XYZ(self.w,0,self.h)
		lnPt4 = XYZ(0,0,self.h)

		#Create line vertices profile 2
		lnPt5 = XYZ(0,self.l,500)
		lnPt6 = XYZ(self.w+100,self.l,500)
		lnPt7 = XYZ(self.w+100,self.l,self.h+500)
		lnPt8 = XYZ(0,self.l,self.h+500)

		# Create Sketch Plane for axis, profile 1 and profile 2
		origin3 = XYZ.Zero		
		plane3 = Plane.CreateByThreePoints(origin3, lnPt5, lnPt6)
		skplane3 = SketchPlane.Create(doc, plane3)
		print(plane3.Normal)

		origin = XYZ.Zero
		normal = Transform.CreateRotation(lnPt2, 0.5*math.pi).OfVector(plane3.Normal)
		print(normal)		 
		plane = Plane.CreateByNormalAndOrigin(normal, origin)
		skplane = SketchPlane.Create(doc, plane)

		origin2 = XYZ(0,self.l,500)				 
		plane2 = Plane.CreateByNormalAndOrigin(normal, origin2)
		skplane2 = SketchPlane.Create(doc, plane2)

		#As our planes changed position we need to rotate points location to new position
		lnPt3_t = Transform.CreateRotation(lnPt2, normal.AngleTo(XYZ.BasisZ)).OfPoint(lnPt3)
		lnPt4_t = Transform.CreateRotation(lnPt2, normal.AngleTo(XYZ.BasisZ)).OfPoint(lnPt4)

		# In profile 2, the rotation axis will change, so we call the CreateRotationAtPoint method
		lnPt7_t = Transform.CreateRotationAtPoint(lnPt2, normal.AngleTo(XYZ.BasisZ), lnPt5).OfPoint(lnPt7)
		lnPt8_t = Transform.CreateRotationAtPoint(lnPt2, normal.AngleTo(XYZ.BasisZ), lnPt5).OfPoint(lnPt8)		

		#create lines profile 1
		line1 = Line.CreateBound(lnPt1, lnPt2)
		line2 = Line.CreateBound(lnPt2, lnPt3_t)
		line3 = Line.CreateBound(lnPt3_t, lnPt4_t)
		line4 = Line.CreateBound(lnPt4_t, lnPt1)

		#create lines profile 2
		line5 = Line.CreateBound(lnPt5, lnPt6)
		line6 = Line.CreateBound(lnPt6, lnPt7_t)
		line7 = Line.CreateBound(lnPt7_t, lnPt8_t)
		line8 = Line.CreateBound(lnPt8_t, lnPt5)

		#create lines axis
		axis_line = Line.CreateBound(lnPt1, lnPt5)
		 
		#create model curves from lines profile 1
		crvA = doc.FamilyCreate.NewModelCurve(line1, skplane)
		crvB = doc.FamilyCreate.NewModelCurve(line2, skplane)
		crvC = doc.FamilyCreate.NewModelCurve(line3, skplane)
		crvD = doc.FamilyCreate.NewModelCurve(line4, skplane)

		#create model curves from lines profile 2
		crvE = doc.FamilyCreate.NewModelCurve(line5, skplane2)
		crvF = doc.FamilyCreate.NewModelCurve(line6, skplane2)
		crvG = doc.FamilyCreate.NewModelCurve(line7, skplane2)
		crvH = doc.FamilyCreate.NewModelCurve(line8, skplane2)

		#create model curves from lines axis
		axis_crv = doc.FamilyCreate.NewModelCurve(axis_line, skplane3)

		#create reference array and append with geometry curve references profile 1
		proarr1 = ReferenceArray()
		proarr1.Append(crvA.GeometryCurve.Reference)
		proarr1.Append(crvB.GeometryCurve.Reference)
		proarr1.Append(crvC.GeometryCurve.Reference)
		proarr1.Append(crvD.GeometryCurve.Reference)

		#create reference array and append with geometry curve references profile 2
		proarr2 = ReferenceArray()
		proarr2.Append(crvE.GeometryCurve.Reference)
		proarr2.Append(crvF.GeometryCurve.Reference)
		proarr2.Append(crvG.GeometryCurve.Reference)
		proarr2.Append(crvH.GeometryCurve.Reference)

		#create reference array and append with geometry curve references axis
		axisarr = ReferenceArray()
		axisarr.Append(axis_crv.GeometryCurve.Reference)

		#create reference array array and append with array references profiles
		profiles_array = ReferenceArrayArray()
		profiles_array.Append(proarr1)
		profiles_array.Append(proarr2)

		sweptBlend = doc.FamilyCreate.NewSweptBlendForm(True, axisarr, profiles_array)



class GaleriaForm(forms.WPFWindow):
	def __init__(self, xaml_file_name):
		forms.WPFWindow.__init__(self, xaml_file_name)
		file_dir = os.path.dirname(__file__)
		self.sectionname.Source = forms.utils.bitmap_from_file(os.path.join(file_dir,'section.png'))
		self.lateralname.Source = forms.utils.bitmap_from_file(os.path.join(file_dir, 'lateral.png'))
		self.wname.Text = '150'
		self.hname.Text = '150'
		self.t1name.Text ='10'
		self.b1name.Text ='10'
		self.e1name.Text ='10'
		self.d1name.Text ='10'
		self.lname.Text ='500'

	def galeria_criar(self,sender,e):
		self.w = int(self.wname.Text)
		self.h = int(self.hname.Text)
		self.t1 = int(self.t1name.Text)
		self.b1 = int(self.b1name.Text)
		self.e1 = int(self.e1name.Text)
		self.d1 = int(self.d1name.Text)
		self.l = int(self.lname.Text)

		start_creation(self)


def start_creation(self):
	t = Transaction(doc, 'Criar Galeria')
 
	t.Start()

	g = Galeria()
	g.create_04(self.w,self.h,self.t1,self.b1,self.e1,self.d1,self.l)

	t.Commit()
 
	#__window__.Close()
 
	
if __name__ == '__main__':
	GaleriaForm("ui.xaml").show(modal=True)



