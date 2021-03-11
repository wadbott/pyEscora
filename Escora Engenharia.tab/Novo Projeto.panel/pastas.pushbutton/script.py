# -*- coding: utf-8 -*-

__title__ = 'Criar\nPastas'
__author__ = 'Wadham Bottacin'

import os
from pyrevit import forms
import datetime

x = datetime.datetime.now()
doc = __revit__.ActiveUIDocument.Document.Title

class DirCreatorForm(forms.WPFWindow):
	def __init__(self, xaml_file_name):
		forms.WPFWindow.__init__(self, xaml_file_name)
		self.docname.Text = str("XXX_" + doc )
		
		

	def selecionar_click(self,sender,e):
		self.folder = forms.pick_folder(title=None, owner=None)
		#print(self.folder)
		try:
			self.pathname.Text = "A árvore de pastas será criada no seguinte caminho:  \n" + self.folder
		except:
			pass


	def criar_click(self, sender, e):
		#print(self.docname.Text)

		LEGENDA = """		
		Legenda:\n

		00-TOPO	Topografia/solos\n
		01-FDC	Fundação\n
		02-EST	Estrutura\n
		03-ARQ	Arquitetura\n
		04-ISP	Inst. Sanitária e Pluvial\n
		05-IHP	Inst. Hidráulica\n
		06-IEP	Inst. Elétrica\n
		07-ITP	Inst. Telefone e Antena\n
		08-GLP	Inst. Gás\n
		09-ICI	Inst. Combate a Incêndio\n
		10-SPDA	Inst. SPDA\n
		11-DOC	Documentos gerais\n
		12-MDL	Modelos BIM\n
		13-MKT	Marketing\n
		14-OUT	Output - Entrega ao cliente\n\n

		Nomeclatura dos arquivos:\n

		CÓDIGO DO PROJETO	XXX\n
		VERSÃO				XX\n
		DISCIPLINA			OLHAR LEGENDA\n
		ETAPA DO PROJETO	ESTUDO ou EXEC\n
		DATA				AAAA-MM\n
		REVISÃO				Rxx\n

		Exemplo:\n
		008-00_ARQ_EXEC_2021-02_R00.rvt\n
		
		"""
		NOMES = []
		NOMES.append("Nomenclatura dos arquivos desse projeto\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "TOPO" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "TOPO" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "FDC" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "FDC" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "EST" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "EST" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "ARQ" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "ARQ" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "ISP" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "ISP" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "IHP" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "IHP" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "IEP" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "IEP" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "ITP" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "ITP" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "GLP" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "GLP" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "ICI" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "ICI" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00\n")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "SPDA" + "_EXEC_" + x.strftime("%Y-%m") + "_R00")
		NOMES.append(self.docname.Text[0:3] + "-00_" + "SPDA" + "_ESTUDO_" + x.strftime("%Y-%m") + "_R00")

		

		SUBS = ['01_'+ self.docname.Text[0:3] + '_DOC',
				'02_'+ self.docname.Text[0:3] + '_MDL',
				'03_'+ self.docname.Text[0:3] + '_MKT',
				'04_'+ self.docname.Text[0:3] + '_OUT'
				]

		SUB_DOCS = ['01_'+ self.docname.Text[0:3] + '_DOC_CONTATO',
				'02_'+ self.docname.Text[0:3] + '_DOC_PROPOSTA',
				'03_'+ self.docname.Text[0:3] + '_DOC_CONTRATO',
				'04_'+ self.docname.Text[0:3] + '_DOC_FOTOS',
				'05_'+ self.docname.Text[0:3] + '_DOC_OUTROS'
				]

		SUB_MDLS = ['01_'+ self.docname.Text[0:3] + '_MDL_TOPO',
					'02_'+ self.docname.Text[0:3] + '_MDL_FDC',
					'03_'+ self.docname.Text[0:3] + '_MDL_EST',
					'04_'+ self.docname.Text[0:3] + '_MDL_ARQ',
					'05_'+ self.docname.Text[0:3] + '_MDL_ISP',
					'06_'+ self.docname.Text[0:3] + '_MDL_IHP',
					'07_'+ self.docname.Text[0:3] + '_MDL_IEP',
					'08_'+ self.docname.Text[0:3] + '_MDL_ITP',
					'09_'+ self.docname.Text[0:3] + '_MDL_GLP',
					'10_'+ self.docname.Text[0:3] + '_MDL_ICI',
					'11_'+ self.docname.Text[0:3] + '_MDL_SPDA',
					'12_'+ self.docname.Text[0:3] + '_MDL_COMP'
					]

		SUB_MKTS = ['01_'+ self.docname.Text[0:3] + '_MKT_ANIMA',
					'02_'+ self.docname.Text[0:3] + '_MKT_PRINTS',
					'03_'+ self.docname.Text[0:3] + '_MKT_VIDEOS',
					'04_'+ self.docname.Text[0:3] + '_MKT_RENDERS'
					]

		SUB_OUTS = ['01_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS',
					'02_'+ self.docname.Text[0:3] + '_OUT_RENDERS',
					'03_'+ self.docname.Text[0:3] + '_OUT_QUANTI',
					'04_'+ self.docname.Text[0:3] + '_OUT_ORÇA',
					'05_'+ self.docname.Text[0:3] + '_OUT_PLANEJ',
					'06_'+ self.docname.Text[0:3] + '_OUT_OUTROS'
					]

		SUB_OUT_PRANCHAS = ['01_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_TOPO',
							'02_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_FDC',
							'03_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_EST',
							'04_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_ARQ',
							'05_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_ISP',
							'06_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_IHP',
							'07_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_IEP',
							'08_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_ITP',
							'09_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_GLP',
							'10_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_ICI',
							'11_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_SPDA',
							'12_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS_COMP'
							]

		try:
			if str(self.folder) == 'None':
				forms.alert(msg='Selecione um destino válido', title='Tente outra vez', ok=True)
			elif os.path.exists(self.folder + '/' + self.docname.Text):
				forms.alert(msg='Já existe uma pasta com este nome', title='Tente outra vez', ok=True)
			else:
				#print("Arquivo será criado" + self.folder + '\\' + self.docname.Text)
				proj_path = os.path.join(self.folder,self.docname.Text)			
				os.mkdir(proj_path)

				with open (os.path.join(proj_path,'legenda.txt'), 'w') as l:
					l.write(LEGENDA)
					l.close()

				with open (os.path.join(proj_path,'nomes.txt'), 'a') as n:
					for nome in NOMES:
						n.write(nome+'\n')

					n.close()

				for SUB in SUBS:					
					os.mkdir(os.path.join(proj_path,SUB))

				doc_path = os.path.join(proj_path,'01_'+ self.docname.Text[0:3] + '_DOC')
				mdl_path = os.path.join(proj_path,'02_'+ self.docname.Text[0:3] + '_MDL')
				mkt_path = os.path.join(proj_path,'03_'+ self.docname.Text[0:3] + '_MKT')
				out_path = os.path.join(proj_path,'04_'+ self.docname.Text[0:3] + '_OUT')

				for SUB_DOC in SUB_DOCS:					
					os.mkdir(os.path.join(doc_path,SUB_DOC))
				for SUB_MDL in SUB_MDLS:					
					os.mkdir(os.path.join(mdl_path,SUB_MDL))
				for SUB_MKT in SUB_MKTS:					
					os.mkdir(os.path.join(mkt_path,SUB_MKT))
				for SUB_OUT in SUB_OUTS:					
					os.mkdir(os.path.join(out_path,SUB_OUT))

				out_pranchas_path = os.path.join(out_path,'01_'+ self.docname.Text[0:3] + '_OUT_PRANCHAS')

				for SUB_OUT_PRANCHA in SUB_OUT_PRANCHAS:
					os.mkdir(os.path.join(out_pranchas_path,SUB_OUT_PRANCHA))


				self.success.Text = "Sucesso!"



		except:
			forms.alert(msg='Selecione um destino primeiro', title='Tente outra vez', ok=True)


if __name__ == '__main__':
	DirCreatorForm("ui.xaml").show(modal=True)



