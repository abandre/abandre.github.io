import pandas as pd
import matplotlib.pyplot as plt
import sys

def atividade1():
	df = pd.read_csv("pesquisa.csv",";")
	print(df.loc[0])
	#df = pd.read_pickle("desempenho.pkl")

def main(DEBUG):
	df = pd.read_pickle("desempenho.pkl")	
	print(df)

if __name__ == "__main__":	
	if len(sys.argv) != 2:
		print("USO: python desempenho.py DEBUG")
		sys.exit(1)	

	DEBUG=int(sys.argv[1])

	#main(DEBUG)
	atividade1()